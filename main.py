from typing import Annotated

string = Annotated[str, "string"] # type: ignore


print("logs") # type: ignore