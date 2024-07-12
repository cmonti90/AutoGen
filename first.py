from jinja2 import Environment, FileSystemLoader

# Define the template directory
template_dir = '.'

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

# Load the template file
template = env.get_template('template.jinja')

# Define data to pass to the template
data = {
    'class_name': 'MyClass',
    'methods': [
        {'return_type': 'void', 'name': 'doSomething', 'args': 'int x, int y'},
        {'return_type': 'int', 'name': 'calculate', 'args': 'double a, double b'}
    ],
    'members': [
        {'type': 'int', 'name': 'x'},
        {'type': 'double', 'name': 'y'}
    ]
}

# Render the template with data
output = template.render(data)

# Print the output or save to a file
print(output)

# Optionally save the output to a file
with open('MyClass.h', 'w') as f:
    f.write(output)