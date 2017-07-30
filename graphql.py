
# Revisit later as not required right now.

class Query:
    def __init__(self, scalar_name):
        self.scalar_name = scalar_name

    def __init__(self, node_name, filters, query):
        self.node_name = node_name
        self.filters = filters
        self.query = query

    def __get_filter_string(self, key, val):
        s = key + ": "
        if val.startswith("$"):
            s += val
        else:
            s += '"' + val + '"';
        return s

    def __get_filters_string(self):
        assert self.filters is not None
        assert isinstance(self.filters, dict)
        return ', '.join([self.__get_filter_string(k, v) for k,v in self.filters.iteritems()])

    def query_string(self):
        if self.scalar_name is not None:
            return self.scalar_name
        else:
            return self.node_name + "(" + self.__get_filters_string() + ")" + self.query.query_string()

