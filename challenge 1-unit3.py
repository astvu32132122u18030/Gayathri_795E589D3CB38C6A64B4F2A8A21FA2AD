def linear_search_product(productlist,targetproduct):
  indices=[]
  for index, product in enumerate(productlist):
    if product==targetproduct:
      indices.append(index) 
  return indices
product=["apple","orange","mango","apple", "grape","banana","apple"]
target="apple"
result=linear_search_product(product, target) 
print(result)