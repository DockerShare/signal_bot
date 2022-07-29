from model.source_information import SourceInformation


def getSourceInformation(envelope):
    return SourceInformation(envelope["sourceUuid"],
                             envelope["sourceNumber"],
                             envelope["sourceName"],
                             envelope["sourceDevice"])
