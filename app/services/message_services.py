from dataclasses import dataclass

@dataclass
class Message:
    message:str = ""
    code:str = ""
    data:dict = None

@dataclass(init=False)
class MessagesBuilder:
    message:str = ""
    code:str = ""
    data:dict = None

    def add_message(self, message: str) -> "MessagesBuilder":
        self.message += message
        return self
    
    def add_code(self, code: str) -> "MessagesBuilder":
        self.code += code
        return self
    
    def add_data(self, data: dict) -> "MessagesBuilder":    
        self.data = data
        return self
    
    def build(self) -> Message:
        return Message(message= self.message, code= self.code, data= self.data)