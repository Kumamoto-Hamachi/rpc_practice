from abc import ABC, abstractmethod
class BaseServicer(ABC):

    @abstractmethod
    def get_registerer():
        """
        return hoge_pb2_grpc.add_HogeServicer_to_server
        """
        pass

    @classmethod
    def get_name_for_reflection_register(self):
        """
        return fuga_pb2.DESCRIPTOR.services_by_name[self.__name__].full_name
        """
        pass
