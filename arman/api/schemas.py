from drf_yasg import openapi

response_schema = {
    "200": openapi.Response(
        description="Successful Response",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "message": openapi.Schema(type=openapi.TYPE_STRING),
                "status": openapi.Schema(type=openapi.TYPE_INTEGER),
                "data": openapi.Schema(type=openapi.TYPE_OBJECT),
                "status_message": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        examples={
            "application/json": {
                "message": "string",
                "status": 200,
                "data": "object or null",
                "status_message": "string",
            }
        },
    ),
    "400": openapi.Response(
        description="Error: Bad Request",
        schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            title="errors",
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "code": openapi.Schema(type=openapi.TYPE_STRING),
                    "field": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        examples={
            "application/json": {
                "errors": [{"message": "string", "code": "string", "field": "string"}]
            }
        },
    ),
}
