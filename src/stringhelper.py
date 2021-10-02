
class bStringHelper:

    def IsRemovelNeeded(self, stringValue):
        pass

    def StringFormat(self, stringValue, charValue):
        pass


class cStringHelper(bStringHelper):

    def IsRemovelNeeded(self, stringValue):
        if '\n' in stringValue:
            return '\n'
        elif '\r' in stringValue:
            return '\r'
        return ''

    def StringFormat(self, stringValue, charValue):
        return stringValue.replace(charValue, '')

