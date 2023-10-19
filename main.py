import argparse
from templates.template_factory import TemplateType, template_factory


def main():
    parser = argparse.ArgumentParser(description='Parser for main.py')

    # Add positional/required argument
    parser.add_argument('--template', type=str, help=f'''Template to be used. Valid templates are: {
    ", ".join([t.value for t in TemplateType])
    }''')

    args = parser.parse_args()
    
    
    template = template_factory(args.template)

    print(template.get_df())
 

if __name__ == '__main__':
    main()
