# Table

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Уникальный ID столика (сквозной идентификатор по всем ресторанам в системе) | 
**name** | **OneOfTableName** | Название или номер столика в ресторане | 
**is_available** | **bool** | Доступность столика для бронирования | 
**place_id** | **int** | Уникальный ID ресторана | 
**available_date_time** | **datetime** | Дата и время свободные для бронирования | 
**tag** | [**TableTag**](TableTag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

