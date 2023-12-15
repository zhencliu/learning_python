class IscsiAccessInfo(object):
    """ISCSI image access: initiator + StorageSecret(u/p)"""

    def __init__(self, image, data, data_format, secret_type, initiator):
        self.storage_type = 'iscsi-direct'
        self.initiator = initiator
        self.secret = StorageSecret(image, data, data_format,
                                    secret_type) if data and secret_type else None

    @classmethod
    def access_info_define_by_params(cls, image, params,
                                     secret_type='password'):
        initiator = params.get('initiator')
        data = params.get('chap_passwd')
        data_format = params.get("data_format", "raw")
        return cls(image, data, data_format, secret_type,
                   initiator) if data and secret_type or initiator else None


class CephAccessInfo(object):
    """Ceph image access: StorageSecret(u/p)"""

    def __init__(self, image, data, data_format, secret_type):
        self.storage_type = 'ceph'
        self.secret = StorageSecret(image, data, data_format,
                                    secret_type) if data and secret_type else None

    @classmethod
    def access_info_define_by_params(cls, image, params, secret_type='key'):
        data = params.get('ceph_key')
        data_format = params.get("data_format", "base64")
        return cls(image, data, data_format,
                   secret_type) if data and secret_type else None

    def _retrieve_access_info(image, params):
        """Create image access info object for qemu-img use"""
        enable_ceph = params.get("enable_ceph", "no") == "yes"
        if enable_ceph:
            # Now only ceph image access requires secret object by qemu-img,
            # and only 'password-secret' is supported
            secret_type = 'password'
            return storage.CephAccessInfo.access_info_define_by_params(image,
                                                                       params,
                                                                       secret_type)
        return None
