from google.protobuf import json_format
import json

from .base import BaseServicer

# 「grpc」パッケージと、grpc_tools.protocによって生成したパッケージをimportする
import club_pb2
import club_pb2_grpc


# クラブ情報の読み込み
CLUB_DB = "./json_data/club.json"
with open(CLUB_DB, mode="r") as fp:
    clubs = json.load(fp)

class ClubManager(club_pb2_grpc.ClubManagerServicer, BaseServicer):
    """
    サービス定義から生成されたクラスを継承して、
    定義したリモートプロシージャに対応するメソッドを実装する。
    クライアントが引数として与えたメッセージに対応するオブジェクト
    context引数にはRPCに関する情報を含むオブジェクトが渡される
    """
    @staticmethod
    def get_registerer():
        return club_pb2_grpc.add_ClubManagerServicer_to_server

    @classmethod
    def get_name_for_reflection_register(self) -> str:
        return club_pb2.DESCRIPTOR.services_by_name[self.__name__].full_name

    def GetClub(self, request: club_pb2.ClubRequest, context):
        """
        クラブ情報を取得する
        """
        # クライアントが送信した引数はrequest引数に格納され、
        # このオブジェクトに対しては一般的なPythonオブジェクトと
        # 同様の形でプロパティにアクセスできる
        club_id = request.id

        # ユーザー情報はユーザーIDを文字列に変換したものをキーとする辞書型データ
        if str(club_id) not in clubs:
            # 該当するユーザーが存在しない場合エラーを返す
            return club_pb2.ClubResponse(error=True, message="not found")
        club = clubs[str(club_id)]

        # 戻り値として返すClubオブジェクトを作成する
        result = club_pb2.Club(
            id=club["id"],
            name=club["name"],
            address=club["address"],
            user_id_list=club["user_id_list"],
        )
        # ClubResponseオブジェクトを返す
        return club_pb2.ClubResponse(error=False, club=result)

