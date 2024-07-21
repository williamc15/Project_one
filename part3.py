class NamespaceManager:
    def __init__(self):
        self._namespace = {}

    def set_variable(self, name, value):
        self._namespace[name] = value

    def get_variable(self, name):
        if name not in self._namespace:
            raise KeyError(f"Variable '{name}' not found in namespace")
        return self._namespace[name]

    def delete_variable(self, name):
        if name not in self._namespace:
            raise KeyError(f"Variable '{name}' not found in namespace")
        del self._namespace[name]

    def list_variables(self):
        return list(self._namespace.keys())

    def execute(self, code):
        # Create a copy of the namespace to avoid modifying the original directly
        local_namespace = dict(self._namespace)
        
        # Execute the code within the context of the local namespace
        exec(code, globals(), local_namespace)
        
        # Update the original namespace with any changes
        self._namespace.update(local_namespace)
        
        # Return the last evaluated expression, if any
        try:
            return eval(code.split('\n')[-1], globals(), self._namespace)
        except:
            return None

# Example usage and testing
if __name__ == "__main__":
    nm = NamespaceManager()
    
    nm.set_variable("x", 10)
    nm.set_variable("y", 20)
    
    print(nm.get_variable("x"))  # Should print: 10
    
    print(nm.list_variables())  # Should print: ['x', 'y']
    
    result = nm.execute("""
z = x + y
print(f"The sum is: {z}")
z * 2
    """)
    print("Result:", result)  # Should print: Result: 60
    
    print(nm.get_variable("z"))  # Should print: 30
    
    nm.delete_variable("y")
    
    try:
        nm.get_variable("y")
    except KeyError as e:
        print(e)  # Should print: "Variable 'y' not found in namespace"
