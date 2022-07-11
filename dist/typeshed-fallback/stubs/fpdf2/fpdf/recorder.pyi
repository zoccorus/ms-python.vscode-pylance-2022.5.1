from typing import Any

class FPDFRecorder:
    pdf: Any
    accept_page_break: bool
    def __init__(self, pdf, accept_page_break: bool = ...) -> None: ...
    def __getattr__(self, name): ...
    def rewind(self) -> None: ...
    def replay(self) -> None: ...

class CallRecorder:
    def __init__(self, func, calls) -> None: ...
    def __call__(self, *args, **kwargs): ...