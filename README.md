# python-module-example

The only dependency for this application is pandas (see pipfile)

This app allows you to execute the main.py script using different command line arguments. The user can choose which template they want to create. For this simple app, the templates only have a dataframe.

To run the app, call the following command on main.py:

```bash
python main.py
```

You should see a ValueError, indicating that you entered an unknown template type, along with a list of valid template types. To run the script with a template type, run the following command:

```bash
python main.py --template=template1
```

You should now see the DataFrame for template1 (see templates/template.py directory) to verify.