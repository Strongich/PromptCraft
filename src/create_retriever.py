from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from check_model import is_directory_empty

from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain_community.vectorstores.chroma import Chroma


def create_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # check if the local directory contains our vectorDB with our .csv file
    if is_directory_empty("./db/"):
        print("Creating a VectorDB with our .csv file...")
        loader = CSVLoader(
            "./data/imdb_movie_data_2023_1.csv",
            metadata_columns=[
                "Movie Name",
                "Rating",
                "Votes",
                "Meta Score",
                "Genre",
                "PG Rating",
                "Year",
                "Duration",
                "Cast",
                "Director",
            ],
        )
        data = loader.load()
        print(data)
        db = FAISS.from_documents(data, embeddings)
        db.save_local("./db/faiss_index")
        retriever = db.as_retriever()
    else:
        db = FAISS.load_local("./db/faiss_index", embeddings)
        retriever = db.as_retriever()
    return retriever


# def create_retriever(llm):
# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# loader = CSVLoader(
#     "./data/imdb_movie_data_2023_1.csv",
#     metadata_columns=[
#         "Movie Name",
#         "Rating",
#         "Votes",
#         "Meta Score",
#         "Genre",
#         "PG Rating",
#         "Year",
#         "Duration",
#         "Cast",
#         "Director",
#     ],
# )
# data = loader.load()
# metadata_field_info = [
#     AttributeInfo(
#         name="Movie Name",
#         description="A name for the movie.",
#         type="float",
#     ),
#     AttributeInfo(
#         name="Rating",
#         description="A 1-10 rating for the movie.",
#         type="float",
#     ),
#     AttributeInfo(
#         name="Votes",
#         description="The number of votes for the movie.",
#         type="float",
#     ),
#     AttributeInfo(
#         name="Meta Score",
#         description="The 0-100 meta score of the movie.",
#         type="float",
#     ),
#     AttributeInfo(
#         name="Genre",
#         description="The genre of the movie.",
#         type="string",
#     ),
#     AttributeInfo(
#         name="PG Rating",
#         description="The PG rating of the movie.",
#         type="string",
#     ),
#     AttributeInfo(
#         name="Year",
#         description="The year the movie was released.",
#         type="integer",
#     ),
#     AttributeInfo(
#         name="Duration",
#         description="The duration of the movie in minutes.",
#         type="float",
#     ),
#     AttributeInfo(
#         name="Cast",
#         description="The cast of the movie",
#         type="string",
#     ),
#     AttributeInfo(
#         name="Director",
#         description="The name of the movie director",
#         type="string",
#     ),
# ]
# document_content_description = "Brief summary of a movie"
# db = Chroma.from_documents(data, embeddings)
# retriever = SelfQueryRetriever.from_llm(
#     llm, db, document_content_description, metadata_field_info
# )
# return retriever
