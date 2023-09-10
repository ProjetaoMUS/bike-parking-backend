# Backend

## Instalation

It is a good practice to use virtual environments for python projects. To create a virtual environment, run the following command:

```bash
python3 -m venv .venv
```

To activate the virtual environment, run the following command:

```bash
source .venv/bin/activate
```

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Setting local environment variables

To set the local environment variables, create a file named `.env` in the root directory of the project and add the following variables: (you can use the `.env.dist` file as a template)
| Variable   | Description                                      | Example      | Required |
| ---------- | ------------------------------------------------ | ------------ | -------- |
| DEBUG      | If set to `True`, the debug mode will be enabled | `True`       | No       |
| SECRET_KEY | The secret key used by Django                    | `secret_key` | Yes      |

## Applying migrations

To apply migrations, run the following command:

```bash
python manage.py migrate
```

## Running the project

To run the project, run the following command:

```bash
python src/manage.py runserver
```
