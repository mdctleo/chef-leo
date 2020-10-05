#!/usr/bin/env python

from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import ChannelNode, HTML5AppNode, TopicNode, VideoNode, DocumentNode, AudioNode
from ricecooker.classes.files import DocumentFile, VideoFile, AudioFile
from le_utils.constants import licenses
from ricecooker.classes.licenses import get_license
from parser import parse_website, teen_levels, adult_levels

class OpenSchoolBCChef(SushiChef):
    """
    The SushiChef class takes care of uploading channel to Kolibri Studio.
    """
    # f4ab95d0789b3c9ed6f016bd766b60b2e1cdaa56
    # 1. PROVIDE CHANNEL INFO  (replace <placeholders> with your own values)
    ############################################################################
    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'openschool.bc.ca/',       # who is providing the content (e.g. learningequality.org)
        'CHANNEL_SOURCE_ID': 'openschool.bc.ca-en',                   # channel's unique id
        'CHANNEL_TITLE': 'Open School BC Resources',
        'CHANNEL_LANGUAGE': 'en',
        # 'CHANNEL_THUMBNAIL': 'http://yourdomain.org/img/logo.jpg', # (optional) local path or url to image file
        # 'CHANNEL_DESCRIPTION': 'What is this channel about?',      # (optional) description of the channel (optional)
    }

    # 2. CONSTRUCT CHANNEL
    ############################################################################
    def construct_channel(self, *args, **kwargs):
        """
        This method is reponsible for creating a `ChannelNode` object and
        populating it with `TopicNode` and `ContentNode` children.
        """
        # Create channel
        ########################################################################
        channel = self.get_channel(*args, **kwargs)     # uses self.channel_info


        # Create topics to add to your channel
        ########################################################################
        teen_topic = TopicNode(source_id="topic-teen", title="K-12 Resources")
        adult_topic = TopicNode(source_id="topic-adult", title="Adult Continue Education Resources")

        channel.add_child(teen_topic)
        channel.add_child(adult_topic)

        level_map = {}
        for index, teen_level in enumerate(teen_levels):
            level_map[teen_level] = TopicNode(source_id="topic-teen-" + teen_level, title=teen_level)

        for index, adult_level in enumerate(adult_levels):
            level_map[adult_level] = TopicNode(source_id="topic-adult-" + adult_level, title=adult_level)

        for level, subtopics in parse_website().items():
            for subtopic, resources in subtopics.items():
                subtopic_node = TopicNode(source_id=subtopic, title=subtopic)
                for resource in resources:
                    resource_file = DocumentFile(path=resource['link'])
                    resource_pdf = DocumentNode(title=resource['title'], source_id=resource['title'], files=[resource_file], license=get_license(licenses.PUBLIC_DOMAIN))
                    subtopic_node.add_child(resource_pdf)
                level_map[level].add_child(subtopic_node)


        for key, value in level_map.items():
            if key in teen_levels:
                teen_topic.add_child(value)
            elif key in adult_levels:
                adult_topic.add_child(value)


        # the `construct_channel` method returns a ChannelNode that will be
        # processed by the ricecooker framework
        return channel


if __name__ == '__main__':
    """
    This code will run when the sushi chef is called from the command line.
    """
    chef = OpenSchoolBCChef()
    chef.main()