from restclients_core.util.decorators import use_mock

from wheniwork.dao import WhenIWork_DAO


fdao_wheniwork_override = use_mock(WhenIWork_DAO())
