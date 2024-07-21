#Creatin the NamespaceManager class to emulate a Python namespace
class NamespaceManager:
    def __init__(self):
        self._namespace = {}

    
    def set_variable(self, name, value):
        self._namespace[name] = value

    def get_variable(self, name):
        if name not in self._namespace:
            raise KeyError(f"Variable '{name}' not found in namespace")
        
        del self._namespace[name]

    def list_variables(self):
        return list(self._namespace.keys())
    
    def execute(self, code):
        #create a copy of the namespace to avoid modifying the original directly
        local_namespace = dict(self._namespace)

        #execute the code within the context of the local namespace
        exec(code, {}, local_namespace)

        #update the original namespace with any changes
        self._namespace.update(local_namespace)

        #Return the last evaluated expression, if any
        return eval(code.split('\n')[-1],{}, self._namespace)
