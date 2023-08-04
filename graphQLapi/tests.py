from django.test import TestCase
from graphene_django.utils import GraphQLTestCase

class GraphQLCartTest(GraphQLTestCase):
    fixtures = ['cart.json']
    def test_retrieve_by_id(self):
        expected = {
            "data": {
                "cart": {
                "id": "1",
                "cartItems": {
                    "itemName": "Samsung TV 82 Inch",
                    "itemNo": 20
                }
                }
            }
        }

        res = self.query("""{
                cart(id: 1){
                id
                cartItems{
                    itemName
                    itemNo
                }
            }
                         
        }""")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(expected, res.json())
            
