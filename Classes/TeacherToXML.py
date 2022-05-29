from lxml import etree, objectify
from io import BytesIO
from Teachers import Teachers
from Elements import Elements

class TeacherToXML:
    def __init__(self, teachers: Teachers):
        self.teachers = teachers

    def write_file(self):
        root = etree.Element("teach")
        for teacher in self.teachers.get_teachers():
            teacher_element = Elements.create_teacher(teacher)
            root.append(teacher_element)

        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        try:
            with open("Teachers.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding="utf-8", xml_declaration=True)
        except IOError:
            pass