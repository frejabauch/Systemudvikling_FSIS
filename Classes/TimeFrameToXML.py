from lxml import etree, objectify
from io import BytesIO
from Timeframes import TimeFrames
from Elements import Elements

class TimeFrameToXML:
    def __init__(self, timeframes: TimeFrames):
        self.timeframes = timeframes

    def write_file(self):
        root = etree.Element("time")
        for timeframe in self.timeframes:
            timeframe_element = Elements.create_timeframe(timeframe)
            root.append(timeframe_element)

        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        try:
            with open("Timeframe.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding="utf-8", xml_declaration=True)
        except IOError:
            pass