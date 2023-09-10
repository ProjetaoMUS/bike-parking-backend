from drf_spectacular.extensions import OpenApiAuthenticationExtension


class KnoxTokenAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = "knox.auth.TokenAuthentication"
    name = "tokenAuth"  # name used in the schema

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
        }
