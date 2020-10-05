#!/usr/bin/env python

from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import ChannelNode, HTML5AppNode, TopicNode, VideoNode, DocumentNode, AudioNode
from ricecooker.classes.files import DocumentFile, VideoFile, AudioFile
from le_utils.constants import licenses
from ricecooker.classes.licenses import get_license

class TutorialChef(SushiChef):
    """
    The SushiChef class takes care of uploading channel to Kolibri Studio.
    """
    # f4ab95d0789b3c9ed6f016bd766b60b2e1cdaa56
    # 1. PROVIDE CHANNEL INFO  (replace <placeholders> with your own values)
    ############################################################################
    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'tutorial.math.lamar.edu',       # who is providing the content (e.g. learningequality.org)
        'CHANNEL_SOURCE_ID': 'tutorial.math.lamar.edu',                   # channel's unique id
        'CHANNEL_TITLE': 'Paul\'s Online Notes',
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
        # Here we are creating a topic named 'Example Topic'
        algebra_topic = TopicNode(source_id="topic-1", title="Algebra")
        # TODO: Create your topic here
        calculus_topic = TopicNode(source_id="topic-2", title="Calculus I")

        # Now we are adding 'Example Topic' to our channel
        channel.add_child(algebra_topic)
        # TODO: Add your topic to channel here
        channel.add_child(calculus_topic)

        # You can also add subtopics to topics
        # Here we are creating a subtopic named 'Example Subtopic'
        # examplesubtopic = TopicNode(source_id="topic-1a", title="Example Subtopic")
        # # TODO: Create your subtopic here
        # my_subtopic = TopicNode(source_id="topic-2a", title="My Subtopic")
        #
        # # Now we are adding 'Example Subtopic' to our 'Example Topic'
        # exampletopic.add_child(examplesubtopic)
        # # TODO: Add your subtopic to your topic here
        # my_topic.add_child(my_subtopic)


        # Content
        # You can add documents (pdfs and ePubs), videos, audios, and other content
        ########################################################################
        # let's create a document file called 'Example PDF'
        # document_file = DocumentFile(path="http://www.pdf995.com/samples/pdf.pdf")
        # examplepdf = DocumentNode(title="Example PDF", source_id="example-pdf", files=[document_file], license=get_license(licenses.PUBLIC_DOMAIN))
        # TODO: Create your pdf file here (use any url to a .pdf file)
        algebra_file = DocumentFile(path="resources/Alg_Complete.pdf")
        algebrapdf = DocumentNode(title="Algebra PDF", source_id="algebra_topic-pdf", files=[algebra_file], license=get_license(licenses.PUBLIC_DOMAIN))

        calculus_file = DocumentFile(path="resources/CalcI_Complete.pdf")
        calculuspdf = DocumentNode(title="Calculus I PDF", source_id="calculus_topic-pdf", files=[calculus_file], license=get_license(licenses.PUBLIC_DOMAIN))

        # # We are also going to add a video file called 'Example Video'
        # video_file = VideoFile(path="https://ia600209.us.archive.org/27/items/RiceChef/Rice Chef.mp4")
        # fancy_license = get_license(licenses.SPECIAL_PERMISSIONS, description='Special license for ricecooker fans only.', copyright_holder='The chef video makers')
        # examplevideo = VideoNode(title="Example Video", source_id="example-video", files=[video_file], license=fancy_license)
        # # TODO: Create your video file here (use any url to a .mp4 file)
        #
        # # Finally, we are creating an audio file called 'Example Audio'
        # audio_file = AudioFile(path="https://ia802508.us.archive.org/5/items/testmp3testfile/mpthreetest.mp3")
        # exampleaudio = AudioNode(title="Example Audio", source_id="example-audio", files=[audio_file], license=get_license(licenses.PUBLIC_DOMAIN))
        # # TODO: Create your audio file here (use any url to a .mp3 file)
        #
        # # Now that we have our files, let's add them to our channel
        # channel.add_child(examplepdf) # Adding 'Example PDF' to your channel
        # exampletopic.add_child(examplevideo) # Adding 'Example Video' to 'Example Topic'
        # examplesubtopic.add_child(exampleaudio) # Adding 'Example Audio' to 'Example Subtopic'

        algebra_topic.add_child(algebrapdf)
        calculus_topic.add_child(calculuspdf)

        # TODO: Add your pdf file to your channel
        # TODO: Add your video file to your topic
        # TODO: Add your audio file to your subtopic


        # the `construct_channel` method returns a ChannelNode that will be
        # processed by the ricecooker framework
        return channel


if __name__ == '__main__':
    """
    This code will run when the sushi chef is called from the command line.
    """
    chef = TutorialChef()
    chef.main()