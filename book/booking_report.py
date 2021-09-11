class BookingReport:
    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name(
            'sr_property_block'
        )

    def pull_titles(self):
        collection = []
        for deal in self.deal_boxes:
            hotel_names = deal.find_element_by_class_name(
                'sr-hotel__name'
            ).get_attribute('innerHTML').strip()

            hotel_price = deal.find_element_by_class_name(
                'bui-price-display__value'
            ).get_attribute('innerHTML').strip()

            hotel_score = deal.get_attribute(
                'data-score'
            ).strip()

            collection.append(
                [hotel_names, hotel_price, hotel_score]
            )
        return collection