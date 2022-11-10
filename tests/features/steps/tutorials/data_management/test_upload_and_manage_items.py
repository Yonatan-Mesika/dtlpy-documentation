import behave
import os
from docs_build.tutorials_templates.data_management.upload_and_manage_items.scripts import Scripts


@behave.when(u'I prepared test upload and manage items "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': section1_prepare,
        'section2': section2_prepare,
        'section3': section3_prepare,
        'section4': section4_prepare,
        'section5': section5_prepare,
    }

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    context.scripts.project_name1 = context.project.name
    context.scripts.dataset_name1 = context.dataset.name

    context.local_path_items = []
    for i in range(3):
        context.local_path_items.append(os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                     'sample_datasets/FruitImage/items/train/apple_{}.jpg'.format(i+1)))

    context.scripts.local_path_item1 = context.local_path_items[0]
    context.scripts.local_path_item2 = context.local_path_items[1]
    context.scripts.local_path_item3 = context.local_path_items[2]
    context.scripts.remote_path1 = '/FruitImage'


def section2_prepare(context):
    context.scripts.project_name2 = context.project.name
    context.scripts.dataset_name2 = context.dataset.name
    context.scripts.local_path2 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                               'sample_datasets/FruitImage/items/train/apple_4.jpg')
    context.scripts.remote_path2 = '/FruitImage'


def section3_prepare(context):
    context.scripts.project3 = context.project
    context.scripts.dataset_name3 = context.dataset.name
    context.scripts.file_name3 = 'flower.jpg'


def section4_prepare(context):
    context.scripts.item4 = context.item


def section5_prepare(context):
    # dataset_id = getattr(self, 'dataset_id5', 'id')
    # ''' First item and info attached: '''
    # local_path1 = getattr(self, 'first_local_path5', r"E:\TypesExamples\000000000064.jpg")
    # local_annotations_path1 = getattr(self, 'first_local_annotations_path5', r"E:\TypesExamples\000000000776.json")
    # ''' Second item and info attached: '''
    # local_path2 = getattr(self, 'second_local_path5', r"E:\TypesExamples\000000000776.jpg")
    # local_annotations_path2 = getattr(self, 'second_local_annotations_path5', r"E:\TypesExamples\000000000776.json")
    context.scripts.project = context.project
    context.scripts.dataset = context.dataset
    context.scripts.dataset_clone = context.project.datasets.get(dataset_name=context.dataset.name + '-clone')
    context.scripts.merge_name = context.dataset.name + '-merge'


@behave.then(u'I run test upload and manage items "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': context.scripts.section1,
        'section2': context.scripts.section2,
        'section3': context.scripts.section2,
        'section4': context.scripts.section2,
        'section5': context.scripts.section2,
    }

    try:
        sections_list[section_name]()

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)



