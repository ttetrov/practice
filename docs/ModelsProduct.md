# ModelsProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | 
**image_url** | **str** |  | [optional] 
**name** | **str** |  | 
**photos** | **List[str]** |  | [optional] 
**price** | **float** |  | 
**product_id** | **str** |  | [optional] 
**quantity** | **int** |  | 
**rating** | **int** |  | 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_product import ModelsProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsProduct from a JSON string
models_product_instance = ModelsProduct.from_json(json)
# print the JSON string representation of the object
print(ModelsProduct.to_json())

# convert the object into a dict
models_product_dict = models_product_instance.to_dict()
# create an instance of ModelsProduct from a dict
models_product_from_dict = ModelsProduct.from_dict(models_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


