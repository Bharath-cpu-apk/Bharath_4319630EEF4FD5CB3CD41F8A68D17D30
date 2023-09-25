def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices
product=["apple","bnana","apple","orange","bana","mango","apple"]
target= "apple"
target2="shoes"
result=linearsearchproduct(product,target)
print(result)