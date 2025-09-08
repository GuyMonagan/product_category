class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(f"{cls_name} создан с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)
