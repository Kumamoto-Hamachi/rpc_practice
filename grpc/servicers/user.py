from google.protobuf import json_format
from typing import List
from collections.abc import Iterable
import json


# 「grpc」パッケージと、grpc_tools.protocによって生成したパッケージをimportする
import user_pb2
import user_pb2_grpc


# ユーザー情報の読み込み
USER_DB = "./json_data/users.json"
with open(USER_DB, mode="r") as fp:
    users = json.load(fp)


class UserManager(user_pb2_grpc.UserManagerServicer):
    """
    サービス定義から生成されたクラスを継承して、
    定義したリモートプロシージャに対応するメソッドを実装する。
    クライアントが引数として与えたメッセージに対応するオブジェクト
    context引数にはRPCに関する情報を含むオブジェクトが渡される
    """

    def GetUser(self, request: user_pb2.UserRequest, context):
        """
        Unary RPC(Simple RPC)
        ユーザー情報を取得する
        """
        # クライアントが送信した引数はrequest引数に格納され、
        # このオブジェクトに対しては一般的なPythonオブジェクトと
        # 同様の形でプロパティにアクセスできる
        user_id = request.id

        # ユーザー情報はユーザーIDを文字列に変換したものをキーとする辞書型データ
        if str(user_id) not in users:
            # 該当するユーザーが存在しない場合エラーを返す
            return user_pb2.UserResponse(error=True, message="not found")
        user = users[str(user_id)]

        # 戻り値として返すUserオブジェクトを作成する
        result = user_pb2.User(
            id=user["id"],
            nickname=user["nickname"],
            mail_address=user["mail_address"],
            user_type=user_pb2.User.UserType.Value(user["user_type"]),
        )
        print("result.user_type", result.user_type, type(result.user_type))  # debug

        # UserResponseオブジェクトを返す
        return user_pb2.UserResponse(error=False, user=result)

    def AddUser(self, request: user_pb2.User, context):
        """
        Unary RPC(Simple RPC)
        新規にユーザー情報を登録する
        """
        # クライアントが送信した引数はrequest引数に格納され、
        # このオブジェクトに対しては一般的なPythonオブジェクトと
        # 同様の形でプロパティにアクセスできる
        user_id = request.id

        # ユーザー情報はユーザーIDを文字列に変換したものをキーとする辞書型データ
        # なので、適宜文字列型に変換して使用している
        if str(user_id) in users:
            # 該当するユーザーが既に存在している場合エラーを返す
            return user_pb2.UserResponse(error=True, message="already exist")

        # 新規登録用及び戻り値として返すUserオブジェクトを作成する
        result = user_pb2.User(
            id=request.id,
            nickname=request.nickname,
            mail_address=request.mail_address,
            user_type=request.user_type,
        )
        # preserving_proto_field_nameでcamelCaseがsnake_caseに変換される
        users[str(request.id)] = json_format.MessageToDict(
            result, preserving_proto_field_name=True
        )
        with open(USER_DB, mode="w") as f:
            json.dump(users, f)

        # UserResponseオブジェクトを返す
        return user_pb2.UserResponse(error=False, user=result)

    def CountAlreadyUsers(self, request_iter: Iterable[user_pb2.UserRequest], context):
        """
        Client streaming RPC(Request-streaming RPC)
        複数渡されたユーザーidのうち既に存在している人数を取得する
        """
        user_cnt = 0
        for request in request_iter:
            user_id = request.id
            # ユーザー情報はユーザーIDを文字列に変換したものをキーとする辞書型データ
            if str(user_id) in users:
                # 該当するユーザーが存在するならカウント
                user_cnt += 1

        # UserCntResponseオブジェクトを返す
        return user_pb2.UserCntResponse(error=False, user_cnt=user_cnt)

    def GetUsersByType(self, request: user_pb2.UserTypeRequest, context):
        """
        Server streaming RPC(Response-streaming RPC)
        渡されたユーザータイプと同じユーザーを複数返す
        """
        user_id_list = [u for u in users]
        print("user_id_list", user_id_list)  # debug
        result_list = []
        for u_id in user_id_list:
            user = users[u_id]
            # Name(数字), Value(NORMAL)とか
            if user_pb2.User.UserType.Name(request.user_type) == user["user_type"]:
                print(f"{user['id']}---該当あり---")
                result = user_pb2.User(
                    id=user["id"],
                    nickname=user["nickname"],
                    mail_address=user["mail_address"],
                    user_type=user_pb2.User.UserType.Value(user["user_type"]),
                )
                yield user_pb2.UserResponse(error=False, user=result)
        # 何も返さない条件が来てもエラーにならない

    def GetUsersByIds(self, request_iter: Iterable[user_pb2.UserRequest], context):
        """
        Bidrectional streaming RPC
        複数渡されたユーザーidのうち存在しているUserを返す
        """
        user_list = []
        for request in request_iter:
            user_id = request.id
            # ユーザー情報はユーザーIDを文字列に変換したものをキーとする辞書型データ
            if str(user_id) in users:
                user = users[str(user_id)]
                user_list.append(user)
        for user in user_list:
            result = user_pb2.User(
                id=user["id"],
                nickname=user["nickname"],
                mail_address=user["mail_address"],
                user_type=user_pb2.User.UserType.Value(user["user_type"]),
            )
            yield user_pb2.UserResponse(error=False, user=result)
