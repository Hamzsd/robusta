from robusta.core.sinks.sink_base_params import SinkBaseParams
from robusta.core.sinks.sink_config import SinkConfigBase


class MailSinkParams(SinkBaseParams):
    toAddress: str
    fromAddress: str
    password: str

class SlackSinkConfigWrapper(SinkConfigBase):
    mail_sink: MailSinkParams

    def get_params(self) -> SinkBaseParams:
        return self.mail_sink
