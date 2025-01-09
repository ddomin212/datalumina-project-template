"""
Pointa je aby AI nemuselo spouštět Edmund platformu pro svoji práci
  Dostaneme Abstraktní třídy (jako třeba ten logger) které místo komplexní implementace (ukládání logů do DB) nahradíš jednoduchou (print()), jako třeba ty dvě uvedeny pod tímhle
"""
class BaseParserLogger(ABC):
    @abstractmethod
    def log(self, *args, **kwargs):
        pass
    @abstractmethod
    def increment_progress(self, by: int):
        pass

class PrintLogger(BaseParserLogger):

    def __init__(self, document_id):
        self.progress_bar = 0
        self.document_id = document_id

    def log(self, *args, **kwargs) -> None:
        print(self.document_id, *args, **kwargs)

    def increment_progress(self, by:int):
        self.progress_bar += by
        self.log(f"{self.document_id}: {self.progress_bar=}%")

class SqlLogger(BaseParserLogger):
    def log(self, *args, **kwargs) -> None:
        # TODO Log to DB
        pass

    def increment_progress(self, by:int):
        # TODO Log to DB
        pass

"""
Indexing Pipeline = hlavní zodpovědnost je dostat data z dokumentu do databáze (což většinou zahrnuje nějaký parser, např PDF nebo SVG).
Má dvě metody aby se data dala nahrát a taky smazat (v případě aktualizace). 

Bude vracet stav nahrání (asi bool) a případně updatovat nějaký progress bar (na FE). Na předávání dat mezi touhle indexing pipeline a retrieval pipeline bude sloužit samotná databáze (vektor, graf)
"""
@dataclass
class AIConfig:
    top_p:int
    top_k:int

@dataclass 
class DBConfig
    database_connector:str


class IndexingPipeline():

    # def __init__(config: Config, db_config: DBConfig):
    #     pass

    @abstractmethod
    def parse(self, document: io.IOBase, document_id: int, abstract_backend_logger: BaseLogger, project_id: int) -> bool:
        pass

    @abstractmethod
    def delete(self) -> bool:
        pass

"""
Retreival pipeline - bude nějakým způsobem dostazovat data v databázi a vracet textové chunks jako kontext pro LLM
"""

class BaseRetreivalPipeline(ABC):

    # def __init__(config: Config, db_config: DBConfig):
    #     pass

    @abstractmethod
    def query(self, document: io.IOBase, document_id: int, abstract_backend_logger: BaseLogger, project_id: int) -> [str]:
        pass