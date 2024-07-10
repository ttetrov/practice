# openapi_client.ProductsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_post**](ProductsApi.md#products_post) | **POST** /products | Create new product
[**products_product_id_get**](ProductsApi.md#products_product_id_get) | **GET** /products/{product_id} | Get product by id
[**products_product_id_put**](ProductsApi.md#products_product_id_put) | **PUT** /products/{product_id} | Update single product
[**products_search_get**](ProductsApi.md#products_search_get) | **GET** /products/search | Search product


# **products_post**
> ModelsProduct products_post()

Create new product

Create new single product

### Example


```python
import openapi_client
from openapi_client.models.models_product import ModelsProduct
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProductsApi(api_client)

    try:
        # Create new product
        api_response = api_instance.products_post()
        print("The response of ProductsApi->products_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsProduct**](ModelsProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_get**
> ModelsProduct products_product_id_get(product_id)

Get product by id

Get single product by id

### Example


```python
import openapi_client
from openapi_client.models.models_product import ModelsProduct
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProductsApi(api_client)
    product_id = 'product_id_example' # str | product id

    try:
        # Get product by id
        api_response = api_instance.products_product_id_get(product_id)
        print("The response of ProductsApi->products_product_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_product_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| product id | 

### Return type

[**ModelsProduct**](ModelsProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_put**
> ModelsProduct products_product_id_put(product_id)

Update single product

Update single product by id

### Example


```python
import openapi_client
from openapi_client.models.models_product import ModelsProduct
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProductsApi(api_client)
    product_id = 'product_id_example' # str | product id

    try:
        # Update single product
        api_response = api_instance.products_product_id_put(product_id)
        print("The response of ProductsApi->products_product_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_product_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| product id | 

### Return type

[**ModelsProduct**](ModelsProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_search_get**
> ModelsProductsList products_search_get(search=search, page=page, size=size)

Search product

Search product by name or description

### Example


```python
import openapi_client
from openapi_client.models.models_products_list import ModelsProductsList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProductsApi(api_client)
    search = 'search_example' # str | search text (optional)
    page = 'page_example' # str | page number (optional)
    size = 'size_example' # str | number of elements (optional)

    try:
        # Search product
        api_response = api_instance.products_search_get(search=search, page=page, size=size)
        print("The response of ProductsApi->products_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search text | [optional] 
 **page** | **str**| page number | [optional] 
 **size** | **str**| number of elements | [optional] 

### Return type

[**ModelsProductsList**](ModelsProductsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

