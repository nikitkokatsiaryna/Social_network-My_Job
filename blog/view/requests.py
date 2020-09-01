import re


def get(self, request, *params):
    if re.match(r'.*new/?$', request.path):
        return self.new(request, *params)
    elif re.match(r'.*edit/?$', request.path):
        return self.edit(request, *params)
    elif re.match(r'.*(\d+)/?$', request.path):
        return self.show(request, *params)
    else:
        return self.index(request, *params)


def post(self, request, *params):
    if '_method' in request.POST:
        if request.POST['_method'].lower() == 'patch':
            return self.patch(request, *params)
        elif request.POST['_method'].lower() == 'delete':
            return self.delete(request, *params)
    else:
        return self.create(request, *params)


def patch(self, request, *params):
    return self.update(request, *params)


def delete(self, request, *params):
    self.destroy(request, *params)
