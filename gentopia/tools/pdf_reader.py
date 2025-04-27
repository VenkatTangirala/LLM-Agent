from pypdf import PdfReader
from typing import AnyStr
from urllib import request
from gentopia.tools.basetool import *
from io import StringIO,BytesIO
 
import openai

class PdfReaderOnlineArgs(BaseModel):
    query: str = Field(..., description="a pdf reader to summarize")

class PdfReaderSearch(BaseTool):
    name = "pdf_reader"
    description = ("PDF reader to summarize"
                   "Input should be a link to PDF paper")
    
    args_schema: Optional[Type[BaseModel]] = PdfReaderOnlineArgs
    print(args_schema)

    

    def _run(self, query: AnyStr) -> str:
        remoteFile = request.urlopen(query).read()
        #remoteFile = remoteFile.decode('utf-8')
        memoryFile = BytesIO(remoteFile)
        #pdfFile = PdfFileReader(memoryFile)
        reader = PdfReader(memoryFile)

        text = ""
        for page in reader.pages:
            text+=page.extract_text()+"\n"
        
        return text[0:10000]

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = PdfReaderSearch()._run("Attention for transformer")
    print(ans)
    



