# Patches for filebrowser forms.

import wrapt


@wrapt.patch_function_wrapper('filebrowser.forms', 'CreateDirForm.clean_name')
def create_dir_form__clean_name(wrapped, instance, args, kwargs):
    # TODO: validate against the base path
    pass


# TODO: the same for ChangeForm
