# -*- coding: utf-8 -*-

#%%
from Warehouse import recalculate_quality, Product


#def recalculate_quality(product):
    #if product.name == "potato":
        #product.quality = product.quality - 0.5
    #elif product.name == "cheese":
        #product.quality = product.quality - 2
    #else:
        #if product.quality < 5:
             #product.quality -= 3

potato1=Product("potato",8)
cheese1=Product("cheese",6)
onion1=Product("onion",10)
apple1=Product("apple",5)
avocado1=Product("avocado",4)

potato2=Product("potato",15)
cheese2=Product("cheese",20)
onion2=Product("onion",10)
apple2=Product("apple",6)
avocado2=Product("avocado",5)

potato3=Product("potato",4)
cheese3=Product("cheese",4)
onion3=Product("onion",4)
apple3=Product("apple",3)
avocado3=Product("avocado",3)

potato4=Product("potato",0)
cheese4=Product("cheese",1)
onion4=Product("onion",2)
apple4=Product("apple",2)
avocado4=Product("avocado",0)

potato5=Product("potato",2.5)
cheese5=Product("cheese",4.5)
onion5=Product("onion",3.5)
apple5=Product("apple",4.5)
avocado5=Product("avocado",5.5)

def test_recalculate_quality_can_differ_between_products():
    recalculate_quality(potato1)
    assert potato1.quality==7.5
    recalculate_quality(cheese1)
    assert cheese1.quality==4
    recalculate_quality(onion1)
    assert onion1.quality==10
    recalculate_quality(apple1)
    assert apple1.quality==5
    recalculate_quality(avocado1)
    assert avocado1.quality==1
    
    
def test_recalculate_quality_more_than_and_equal_5():
    recalculate_quality(potato2)
    assert potato2.quality==14.5
    recalculate_quality(cheese2)
    assert cheese2.quality==18
    recalculate_quality(onion2)
    assert onion2.quality==10
    recalculate_quality(apple2)
    assert apple2.quality==6
    recalculate_quality(avocado2)
    assert avocado2.quality==5
    
    
def test_recalculate_quality_less_than_5():
    recalculate_quality(potato3)
    assert potato3.quality==3.5
    recalculate_quality(cheese3)
    assert cheese3.quality==2
    recalculate_quality(onion3)
    assert onion3.quality==1
    recalculate_quality(apple3)
    assert apple3.quality==0
    recalculate_quality(avocado3)
    assert avocado3.quality==0
    
    
def test_recalculate_quality_goes_negative():
    recalculate_quality(potato4)
    assert potato4.quality==-0.5
    recalculate_quality(cheese4)
    assert cheese4.quality==-1
    recalculate_quality(onion4)
    assert onion4.quality==-1
    recalculate_quality(apple4)
    assert apple4.quality==-1
    recalculate_quality(avocado4)
    assert avocado4.quality==-3
    
    
def test_recalculate_quality_floatingnumbers():
    recalculate_quality(potato5)
    assert potato5.quality==2
    recalculate_quality(cheese5)
    assert cheese5.quality==2.5
    recalculate_quality(onion5)
    assert onion5.quality==0.5
    recalculate_quality(apple5)
    assert apple5.quality==1.5
    recalculate_quality(avocado5)
    assert avocado5.quality==5.5
    


    
    
    
    