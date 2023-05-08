from kivymd.uix.list import OneLineAvatarIconListItem

class ItemCategoryPopup(OneLineAvatarIconListItem):
    def set_icon(self, instance_check):
        instance_check.active = True
        active = False
        self.on_release = self.toggle_active
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active= False
