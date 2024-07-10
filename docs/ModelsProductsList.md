# ModelsProductsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | [optional] 
**page** | **int** |  | [optional] 
**products** | [**List[ModelsProduct]**](ModelsProduct.md) |  | [optional] 
**size** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.models_products_list import ModelsProductsList

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsProductsList from a JSON string
models_products_list_instance = ModelsProductsList.from_json(json)
# print the JSON string representation of the object
print(ModelsProductsList.to_json())

# convert the object into a dict
models_products_list_dict = models_products_list_instance.to_dict()
# create an instance of ModelsProductsList from a dict
models_products_list_from_dict = ModelsProductsList.from_dict(models_products_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


