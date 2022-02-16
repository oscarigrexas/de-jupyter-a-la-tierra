# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from catfood.items import CatfoodItem
import urllib


class CatSpider(scrapy.Spider):
    name = "cat"
    allowed_domains = ["catfooddb.com"]
    start_urls = ["http://catfooddb.com/"]
    custom_settings = {
        "FEED_URI": "food_%(time)s.csv",
        "FEED_FORMAT": "csv",
    }

    def parse(self, response):
        """Follow links to brand pages"""
        # The cleanest way to get to the brand pages is through the dropdown menu
        path = "//ul[@class='dropdown-menu']/li/a/@href"
        for href in response.xpath(path)[:-6]:
            print(href)
            yield response.follow(href, self.parse_brand)

    def parse_brand(self, response):
        """Follow links to product pages"""
        # All product pages have the .product class
        for href in response.xpath("//td[@class='product']/a/@href"):
            yield response.follow(href, self.printwhatever)

    def printwhatever(self, response):
        """Populate the item CatfoodItem with all the relevant product information"""
        l = ItemLoader(item=CatfoodItem(), response=response)
        # Get the product name from the response url
        name = response.url.split("/")[-1].replace("+", " ")
        name = urllib.parse.unquote(name)
        l.add_value("name", name)
        # Get the brand name from the response url
        brand = response.url.split("/")[-2]
        brand = urllib.parse.unquote(brand)
        l.add_value("brand", brand)
        # Count the number of ingredients paws
        i_paws = len(response.xpath("//i[@class='fa fa-paw ingredients-paws']"))
        l.add_value("ingredients_paws", i_paws)
        # Count the number of nutrition paws
        n_paws = len(response.xpath("//i[@class='fa fa-paw nutrition-paws']"))
        l.add_value("nutrition_paws", n_paws)
        # Get the list of ingredients
        ingredients = response.xpath("//small/text()")[2].extract().split(", ")
        l.add_value("ingredients", ingredients)
        quality_ingredients = response.xpath(
            "//div[contains(@class, 'panel-success')]/div[contains(@class, 'panel-body')]/ul/li/text()"
        ).extract()
        l.add_value("quality_ingredients", quality_ingredients)
        questionable_ingredients = response.xpath(
            "//div[contains(@class, 'panel-danger')]/div[contains(@class, 'panel-body')]/ul/li/text()"
        ).extract()
        l.add_value("questionable_ingredients", questionable_ingredients)
        potential_allergens = response.xpath(
            "//div[contains(@class, 'panel-warning')]/div[contains(@class, 'panel-body')]/ul/li/text()"
        ).extract()
        l.add_value("potential_allergens", potential_allergens)
        # Get nutritional values as a list and assign them
        ga_list = response.xpath(
            '//div[@class="panel panel-default"]'
            '[div[@class="panel-heading"]/h3/text()="Guaranteed Analysis"]'
            '/div[@class="panel-body"]'
            '/div/div[contains(@class,"text-right")]/text()'
        ).extract()
        dma_list = response.xpath(
            '//div[@class="panel panel-default"]'
            '[div[@class="panel-heading"]/h3/text()="Dry Matter Analysis"]'
            '/div[@class="panel-body"]'
            '/div/div[contains(@class,"text-right")]/text()'
        ).extract()
        l.add_value(
            None,
            {
                "ga_prot": ga_list[0],
                "ga_fat": ga_list[1],
                "ga_fiber": ga_list[2],
                "ga_carbs": ga_list[3],
                "ga_ash": ga_list[4],
                "ga_moist": ga_list[5],
                "dma_prot": dma_list[0],
                "dma_fat": dma_list[1],
                "dma_fiber": dma_list[2],
                "dma_carbs": dma_list[3],
                "dma_ash": dma_list[4],
                "dma_cals": dma_list[-1],
            },
        )
        fooditem = l.load_item()
        yield fooditem
