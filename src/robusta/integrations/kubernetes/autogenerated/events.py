# This file was autogenerated. Do not edit.

import logging
import traceback
from dataclasses import dataclass
from abc import abstractmethod
from hikaru.model import (
    Pod,
    ReplicaSet,
    DaemonSet,
    Deployment,
    StatefulSet,
    Service,
    Event,
    HorizontalPodAutoscaler,
    Node,
    ClusterRole,
    ClusterRoleBinding,
    Job,
    Namespace,
    ServiceAccount,
)
from hikaru.utils import Response
from pydantic import BaseModel
from typing import Union, Optional, List
from ..base_event import K8sBaseChangeEvent
from ....core.model.events import ExecutionBaseEvent, ExecutionEventBaseParams
from ..custom_models import RobustaPod, RobustaDeployment, RobustaJob
from hikaru.model.rel_1_16.v1 import Pod as v1Pod
from hikaru.model.rel_1_16.v1 import ReplicaSet as v1ReplicaSet
from hikaru.model.rel_1_16.v1 import DaemonSet as v1DaemonSet
from hikaru.model.rel_1_16.v1 import Deployment as v1Deployment
from hikaru.model.rel_1_16.v1 import StatefulSet as v1StatefulSet
from hikaru.model.rel_1_16.v1 import Service as v1Service
from hikaru.model.rel_1_16.v1 import Event as v1Event
from hikaru.model.rel_1_16.v1 import (
    HorizontalPodAutoscaler as v1HorizontalPodAutoscaler,
)
from hikaru.model.rel_1_16.v1 import Node as v1Node
from hikaru.model.rel_1_16.v1 import ClusterRole as v1ClusterRole
from hikaru.model.rel_1_16.v1 import ClusterRoleBinding as v1ClusterRoleBinding
from hikaru.model.rel_1_16.v1 import Job as v1Job
from hikaru.model.rel_1_16.v1 import Namespace as v1Namespace
from hikaru.model.rel_1_16.v1 import ServiceAccount as v1ServiceAccount
from hikaru.model.rel_1_16.v2beta1 import Pod as v2beta1Pod
from hikaru.model.rel_1_16.v2beta1 import ReplicaSet as v2beta1ReplicaSet
from hikaru.model.rel_1_16.v2beta1 import DaemonSet as v2beta1DaemonSet
from hikaru.model.rel_1_16.v2beta1 import Deployment as v2beta1Deployment
from hikaru.model.rel_1_16.v2beta1 import StatefulSet as v2beta1StatefulSet
from hikaru.model.rel_1_16.v2beta1 import Service as v2beta1Service
from hikaru.model.rel_1_16.v2beta1 import Event as v2beta1Event
from hikaru.model.rel_1_16.v2beta1 import (
    HorizontalPodAutoscaler as v2beta1HorizontalPodAutoscaler,
)
from hikaru.model.rel_1_16.v2beta1 import Node as v2beta1Node
from hikaru.model.rel_1_16.v2beta1 import ClusterRole as v2beta1ClusterRole
from hikaru.model.rel_1_16.v2beta1 import (
    ClusterRoleBinding as v2beta1ClusterRoleBinding,
)
from hikaru.model.rel_1_16.v2beta1 import Job as v2beta1Job
from hikaru.model.rel_1_16.v2beta1 import Namespace as v2beta1Namespace
from hikaru.model.rel_1_16.v2beta1 import ServiceAccount as v2beta1ServiceAccount
from hikaru.model.rel_1_16.v2beta2 import Pod as v2beta2Pod
from hikaru.model.rel_1_16.v2beta2 import ReplicaSet as v2beta2ReplicaSet
from hikaru.model.rel_1_16.v2beta2 import DaemonSet as v2beta2DaemonSet
from hikaru.model.rel_1_16.v2beta2 import Deployment as v2beta2Deployment
from hikaru.model.rel_1_16.v2beta2 import StatefulSet as v2beta2StatefulSet
from hikaru.model.rel_1_16.v2beta2 import Service as v2beta2Service
from hikaru.model.rel_1_16.v2beta2 import Event as v2beta2Event
from hikaru.model.rel_1_16.v2beta2 import (
    HorizontalPodAutoscaler as v2beta2HorizontalPodAutoscaler,
)
from hikaru.model.rel_1_16.v2beta2 import Node as v2beta2Node
from hikaru.model.rel_1_16.v2beta2 import ClusterRole as v2beta2ClusterRole
from hikaru.model.rel_1_16.v2beta2 import (
    ClusterRoleBinding as v2beta2ClusterRoleBinding,
)
from hikaru.model.rel_1_16.v2beta2 import Job as v2beta2Job
from hikaru.model.rel_1_16.v2beta2 import Namespace as v2beta2Namespace
from hikaru.model.rel_1_16.v2beta2 import ServiceAccount as v2beta2ServiceAccount


LOADERS_MAPPINGS = {
    "Pod": (True, RobustaPod.readNamespacedPod),
    "ReplicaSet": (True, ReplicaSet.readNamespacedReplicaSet),
    "DaemonSet": (True, DaemonSet.readNamespacedDaemonSet),
    "Deployment": (True, RobustaDeployment.readNamespacedDeployment),
    "StatefulSet": (True, StatefulSet.readNamespacedStatefulSet),
    "Service": (True, Service.readNamespacedService),
    "Event": (True, Event.readNamespacedEvent),
    "HorizontalPodAutoscaler": (
        True,
        HorizontalPodAutoscaler.readNamespacedHorizontalPodAutoscaler,
    ),
    "Node": (False, Node.readNode),
    "ClusterRole": (False, ClusterRole.readClusterRole),
    "ClusterRoleBinding": (False, ClusterRoleBinding.readClusterRoleBinding),
    "Job": (True, RobustaJob.readNamespacedJob),
    "Namespace": (False, Namespace.readNamespace),
    "ServiceAccount": (True, ServiceAccount.readNamespacedServiceAccount),
}


class ResourceLoader:
    @staticmethod
    def read_resource(kind: str, name: str, namespace: str = None) -> Response:
        resource_mapper = LOADERS_MAPPINGS[kind]
        if not resource_mapper:
            raise Exception("resource loader not found")

        if resource_mapper[0]:  # namespaced resource
            return resource_mapper[1](name=name, namespace=namespace)
        else:
            return resource_mapper[1](name=name)


class ResourceAttributes(ExecutionEventBaseParams):
    kind: str
    name: str
    namespace: Optional[str] = None


@dataclass
class KubernetesResourceEvent(ExecutionBaseEvent):
    _obj: Optional[
        Union[
            RobustaPod,
            ReplicaSet,
            DaemonSet,
            RobustaDeployment,
            StatefulSet,
            Service,
            Event,
            HorizontalPodAutoscaler,
            Node,
            ClusterRole,
            ClusterRoleBinding,
            RobustaJob,
            Namespace,
            ServiceAccount,
        ]
    ] = None

    def __init__(
        self,
        obj: Union[
            RobustaPod,
            ReplicaSet,
            DaemonSet,
            RobustaDeployment,
            StatefulSet,
            Service,
            Event,
            HorizontalPodAutoscaler,
            Node,
            ClusterRole,
            ClusterRoleBinding,
            RobustaJob,
            Namespace,
            ServiceAccount,
        ],
        named_sinks: List[str],
    ):
        super().__init__(named_sinks=named_sinks)
        self._obj = obj

    def get_resource(
        self,
    ) -> Optional[
        Union[
            RobustaPod,
            ReplicaSet,
            DaemonSet,
            RobustaDeployment,
            StatefulSet,
            Service,
            Event,
            HorizontalPodAutoscaler,
            Node,
            ClusterRole,
            ClusterRoleBinding,
            RobustaJob,
            Namespace,
            ServiceAccount,
        ]
    ]:
        return self._obj

    @staticmethod
    def from_params(params: ResourceAttributes) -> Optional["KubernetesResourceEvent"]:
        try:
            obj = ResourceLoader.read_resource(
                kind=params.kind, name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load resource {params}", exc_info=True)
            return None
        return KubernetesResourceEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class KubernetesAnyChangeEvent(K8sBaseChangeEvent):
    obj: Optional[
        Union[
            v1HorizontalPodAutoscaler,
            v2beta2Node,
            v2beta1Service,
            v2beta1DaemonSet,
            RobustaDeployment,
            v1ReplicaSet,
            v1DaemonSet,
            v2beta2ClusterRoleBinding,
            v2beta2Namespace,
            v2beta2ReplicaSet,
            v2beta1Event,
            v1Node,
            v1StatefulSet,
            v2beta1ClusterRoleBinding,
            v2beta1Namespace,
            v1ClusterRoleBinding,
            RobustaJob,
            v2beta2HorizontalPodAutoscaler,
            v2beta2DaemonSet,
            v2beta2StatefulSet,
            v2beta2Service,
            v2beta2Event,
            v2beta1HorizontalPodAutoscaler,
            v2beta2ServiceAccount,
            v2beta1ReplicaSet,
            v1Event,
            v1ServiceAccount,
            v1Service,
            v1ClusterRole,
            RobustaPod,
            v2beta1Node,
            v2beta1ServiceAccount,
            v2beta1ClusterRole,
            v2beta2ClusterRole,
            v2beta1StatefulSet,
            v1Namespace,
        ]
    ] = None
    old_obj: Optional[
        Union[
            v1HorizontalPodAutoscaler,
            v2beta2Node,
            v2beta1Service,
            v2beta1DaemonSet,
            RobustaDeployment,
            v1ReplicaSet,
            v1DaemonSet,
            v2beta2ClusterRoleBinding,
            v2beta2Namespace,
            v2beta2ReplicaSet,
            v2beta1Event,
            v1Node,
            v1StatefulSet,
            v2beta1ClusterRoleBinding,
            v2beta1Namespace,
            v1ClusterRoleBinding,
            RobustaJob,
            v2beta2HorizontalPodAutoscaler,
            v2beta2DaemonSet,
            v2beta2StatefulSet,
            v2beta2Service,
            v2beta2Event,
            v2beta1HorizontalPodAutoscaler,
            v2beta2ServiceAccount,
            v2beta1ReplicaSet,
            v1Event,
            v1ServiceAccount,
            v1Service,
            v1ClusterRole,
            RobustaPod,
            v2beta1Node,
            v2beta1ServiceAccount,
            v2beta1ClusterRole,
            v2beta2ClusterRole,
            v2beta1StatefulSet,
            v1Namespace,
        ]
    ] = None

    def get_resource(
        self,
    ) -> Optional[
        Union[
            v1HorizontalPodAutoscaler,
            v2beta2Node,
            v2beta1Service,
            v2beta1DaemonSet,
            RobustaDeployment,
            v1ReplicaSet,
            v1DaemonSet,
            v2beta2ClusterRoleBinding,
            v2beta2Namespace,
            v2beta2ReplicaSet,
            v2beta1Event,
            v1Node,
            v1StatefulSet,
            v2beta1ClusterRoleBinding,
            v2beta1Namespace,
            v1ClusterRoleBinding,
            RobustaJob,
            v2beta2HorizontalPodAutoscaler,
            v2beta2DaemonSet,
            v2beta2StatefulSet,
            v2beta2Service,
            v2beta2Event,
            v2beta1HorizontalPodAutoscaler,
            v2beta2ServiceAccount,
            v2beta1ReplicaSet,
            v1Event,
            v1ServiceAccount,
            v1Service,
            v1ClusterRole,
            RobustaPod,
            v2beta1Node,
            v2beta1ServiceAccount,
            v2beta1ClusterRole,
            v2beta2ClusterRole,
            v2beta1StatefulSet,
            v1Namespace,
        ]
    ]:
        return self.obj


class PodAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class PodEvent(KubernetesResourceEvent):
    def __init__(self, obj: RobustaPod, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_pod(self) -> Optional[RobustaPod]:
        return self._obj

    @staticmethod
    def from_params(params: PodAttributes) -> Optional["PodEvent"]:
        try:
            obj = RobustaPod.readNamespacedPod(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load Pod {params}", exc_info=True)
            return None
        return PodEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class PodChangeEvent(PodEvent, KubernetesAnyChangeEvent):
    obj: Optional[RobustaPod] = None
    old_obj: Optional[RobustaPod] = None

    def get_pod(self) -> Optional[RobustaPod]:
        return self.obj


class ReplicaSetAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class ReplicaSetEvent(KubernetesResourceEvent):
    def __init__(self, obj: ReplicaSet, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_replicaset(self) -> Optional[ReplicaSet]:
        return self._obj

    @staticmethod
    def from_params(params: ReplicaSetAttributes) -> Optional["ReplicaSetEvent"]:
        try:
            obj = ReplicaSet.readNamespacedReplicaSet(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load ReplicaSet {params}", exc_info=True)
            return None
        return ReplicaSetEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class ReplicaSetChangeEvent(ReplicaSetEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1ReplicaSet, v2beta1ReplicaSet, v2beta2ReplicaSet]] = None
    old_obj: Optional[Union[v1ReplicaSet, v2beta1ReplicaSet, v2beta2ReplicaSet]] = None

    def get_replicaset(
        self,
    ) -> Optional[Union[v1ReplicaSet, v2beta1ReplicaSet, v2beta2ReplicaSet]]:
        return self.obj


class DaemonSetAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class DaemonSetEvent(KubernetesResourceEvent):
    def __init__(self, obj: DaemonSet, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_daemonset(self) -> Optional[DaemonSet]:
        return self._obj

    @staticmethod
    def from_params(params: DaemonSetAttributes) -> Optional["DaemonSetEvent"]:
        try:
            obj = DaemonSet.readNamespacedDaemonSet(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load DaemonSet {params}", exc_info=True)
            return None
        return DaemonSetEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class DaemonSetChangeEvent(DaemonSetEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1DaemonSet, v2beta1DaemonSet, v2beta2DaemonSet]] = None
    old_obj: Optional[Union[v1DaemonSet, v2beta1DaemonSet, v2beta2DaemonSet]] = None

    def get_daemonset(
        self,
    ) -> Optional[Union[v1DaemonSet, v2beta1DaemonSet, v2beta2DaemonSet]]:
        return self.obj


class DeploymentAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class DeploymentEvent(KubernetesResourceEvent):
    def __init__(self, obj: RobustaDeployment, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_deployment(self) -> Optional[RobustaDeployment]:
        return self._obj

    @staticmethod
    def from_params(params: DeploymentAttributes) -> Optional["DeploymentEvent"]:
        try:
            obj = RobustaDeployment.readNamespacedDeployment(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load Deployment {params}", exc_info=True)
            return None
        return DeploymentEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class DeploymentChangeEvent(DeploymentEvent, KubernetesAnyChangeEvent):
    obj: Optional[RobustaDeployment] = None
    old_obj: Optional[RobustaDeployment] = None

    def get_deployment(self) -> Optional[RobustaDeployment]:
        return self.obj


class StatefulSetAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class StatefulSetEvent(KubernetesResourceEvent):
    def __init__(self, obj: StatefulSet, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_statefulset(self) -> Optional[StatefulSet]:
        return self._obj

    @staticmethod
    def from_params(params: StatefulSetAttributes) -> Optional["StatefulSetEvent"]:
        try:
            obj = StatefulSet.readNamespacedStatefulSet(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load StatefulSet {params}", exc_info=True)
            return None
        return StatefulSetEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class StatefulSetChangeEvent(StatefulSetEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1StatefulSet, v2beta1StatefulSet, v2beta2StatefulSet]] = None
    old_obj: Optional[
        Union[v1StatefulSet, v2beta1StatefulSet, v2beta2StatefulSet]
    ] = None

    def get_statefulset(
        self,
    ) -> Optional[Union[v1StatefulSet, v2beta1StatefulSet, v2beta2StatefulSet]]:
        return self.obj


class ServiceAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class ServiceEvent(KubernetesResourceEvent):
    def __init__(self, obj: Service, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_service(self) -> Optional[Service]:
        return self._obj

    @staticmethod
    def from_params(params: ServiceAttributes) -> Optional["ServiceEvent"]:
        try:
            obj = Service.readNamespacedService(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load Service {params}", exc_info=True)
            return None
        return ServiceEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class ServiceChangeEvent(ServiceEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1Service, v2beta1Service, v2beta2Service]] = None
    old_obj: Optional[Union[v1Service, v2beta1Service, v2beta2Service]] = None

    def get_service(self) -> Optional[Union[v1Service, v2beta1Service, v2beta2Service]]:
        return self.obj


class EventAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class EventEvent(KubernetesResourceEvent):
    def __init__(self, obj: Event, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_event(self) -> Optional[Event]:
        return self._obj

    @staticmethod
    def from_params(params: EventAttributes) -> Optional["EventEvent"]:
        try:
            obj = Event.readNamespacedEvent(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load Event {params}", exc_info=True)
            return None
        return EventEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class EventChangeEvent(EventEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1Event, v2beta1Event, v2beta2Event]] = None
    old_obj: Optional[Union[v1Event, v2beta1Event, v2beta2Event]] = None

    def get_event(self) -> Optional[Union[v1Event, v2beta1Event, v2beta2Event]]:
        return self.obj


class HorizontalPodAutoscalerAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class HorizontalPodAutoscalerEvent(KubernetesResourceEvent):
    def __init__(self, obj: HorizontalPodAutoscaler, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_horizontalpodautoscaler(self) -> Optional[HorizontalPodAutoscaler]:
        return self._obj

    @staticmethod
    def from_params(
        params: HorizontalPodAutoscalerAttributes,
    ) -> Optional["HorizontalPodAutoscalerEvent"]:
        try:
            obj = HorizontalPodAutoscaler.readNamespacedHorizontalPodAutoscaler(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(
                f"Could not load HorizontalPodAutoscaler {params}", exc_info=True
            )
            return None
        return HorizontalPodAutoscalerEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class HorizontalPodAutoscalerChangeEvent(
    HorizontalPodAutoscalerEvent, KubernetesAnyChangeEvent
):
    obj: Optional[
        Union[
            v1HorizontalPodAutoscaler,
            v2beta1HorizontalPodAutoscaler,
            v2beta2HorizontalPodAutoscaler,
        ]
    ] = None
    old_obj: Optional[
        Union[
            v1HorizontalPodAutoscaler,
            v2beta1HorizontalPodAutoscaler,
            v2beta2HorizontalPodAutoscaler,
        ]
    ] = None

    def get_horizontalpodautoscaler(
        self,
    ) -> Optional[
        Union[
            v1HorizontalPodAutoscaler,
            v2beta1HorizontalPodAutoscaler,
            v2beta2HorizontalPodAutoscaler,
        ]
    ]:
        return self.obj


class NodeAttributes(ExecutionEventBaseParams):
    name: str


@dataclass
class NodeEvent(KubernetesResourceEvent):
    def __init__(self, obj: Node, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_node(self) -> Optional[Node]:
        return self._obj

    @staticmethod
    def from_params(params: NodeAttributes) -> Optional["NodeEvent"]:
        try:
            obj = Node.readNode(name=params.name).obj
        except Exception:
            logging.error(f"Could not load Node {params}", exc_info=True)
            return None
        return NodeEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class NodeChangeEvent(NodeEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1Node, v2beta1Node, v2beta2Node]] = None
    old_obj: Optional[Union[v1Node, v2beta1Node, v2beta2Node]] = None

    def get_node(self) -> Optional[Union[v1Node, v2beta1Node, v2beta2Node]]:
        return self.obj


class ClusterRoleAttributes(ExecutionEventBaseParams):
    name: str


@dataclass
class ClusterRoleEvent(KubernetesResourceEvent):
    def __init__(self, obj: ClusterRole, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_clusterrole(self) -> Optional[ClusterRole]:
        return self._obj

    @staticmethod
    def from_params(params: ClusterRoleAttributes) -> Optional["ClusterRoleEvent"]:
        try:
            obj = ClusterRole.readClusterRole(name=params.name).obj
        except Exception:
            logging.error(f"Could not load ClusterRole {params}", exc_info=True)
            return None
        return ClusterRoleEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class ClusterRoleChangeEvent(ClusterRoleEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1ClusterRole, v2beta1ClusterRole, v2beta2ClusterRole]] = None
    old_obj: Optional[
        Union[v1ClusterRole, v2beta1ClusterRole, v2beta2ClusterRole]
    ] = None

    def get_clusterrole(
        self,
    ) -> Optional[Union[v1ClusterRole, v2beta1ClusterRole, v2beta2ClusterRole]]:
        return self.obj


class ClusterRoleBindingAttributes(ExecutionEventBaseParams):
    name: str


@dataclass
class ClusterRoleBindingEvent(KubernetesResourceEvent):
    def __init__(self, obj: ClusterRoleBinding, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_clusterrolebinding(self) -> Optional[ClusterRoleBinding]:
        return self._obj

    @staticmethod
    def from_params(
        params: ClusterRoleBindingAttributes,
    ) -> Optional["ClusterRoleBindingEvent"]:
        try:
            obj = ClusterRoleBinding.readClusterRoleBinding(name=params.name).obj
        except Exception:
            logging.error(f"Could not load ClusterRoleBinding {params}", exc_info=True)
            return None
        return ClusterRoleBindingEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class ClusterRoleBindingChangeEvent(ClusterRoleBindingEvent, KubernetesAnyChangeEvent):
    obj: Optional[
        Union[
            v1ClusterRoleBinding, v2beta1ClusterRoleBinding, v2beta2ClusterRoleBinding
        ]
    ] = None
    old_obj: Optional[
        Union[
            v1ClusterRoleBinding, v2beta1ClusterRoleBinding, v2beta2ClusterRoleBinding
        ]
    ] = None

    def get_clusterrolebinding(
        self,
    ) -> Optional[
        Union[
            v1ClusterRoleBinding, v2beta1ClusterRoleBinding, v2beta2ClusterRoleBinding
        ]
    ]:
        return self.obj


class JobAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class JobEvent(KubernetesResourceEvent):
    def __init__(self, obj: RobustaJob, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_job(self) -> Optional[RobustaJob]:
        return self._obj

    @staticmethod
    def from_params(params: JobAttributes) -> Optional["JobEvent"]:
        try:
            obj = RobustaJob.readNamespacedJob(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load Job {params}", exc_info=True)
            return None
        return JobEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class JobChangeEvent(JobEvent, KubernetesAnyChangeEvent):
    obj: Optional[RobustaJob] = None
    old_obj: Optional[RobustaJob] = None

    def get_job(self) -> Optional[RobustaJob]:
        return self.obj


class NamespaceAttributes(ExecutionEventBaseParams):
    name: str


@dataclass
class NamespaceEvent(KubernetesResourceEvent):
    def __init__(self, obj: Namespace, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_namespace(self) -> Optional[Namespace]:
        return self._obj

    @staticmethod
    def from_params(params: NamespaceAttributes) -> Optional["NamespaceEvent"]:
        try:
            obj = Namespace.readNamespace(name=params.name).obj
        except Exception:
            logging.error(f"Could not load Namespace {params}", exc_info=True)
            return None
        return NamespaceEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class NamespaceChangeEvent(NamespaceEvent, KubernetesAnyChangeEvent):
    obj: Optional[Union[v1Namespace, v2beta1Namespace, v2beta2Namespace]] = None
    old_obj: Optional[Union[v1Namespace, v2beta1Namespace, v2beta2Namespace]] = None

    def get_namespace(
        self,
    ) -> Optional[Union[v1Namespace, v2beta1Namespace, v2beta2Namespace]]:
        return self.obj


class ServiceAccountAttributes(ExecutionEventBaseParams):
    name: str
    namespace: str


@dataclass
class ServiceAccountEvent(KubernetesResourceEvent):
    def __init__(self, obj: ServiceAccount, named_sinks: List[str]):
        super().__init__(obj=obj, named_sinks=named_sinks)

    def get_serviceaccount(self) -> Optional[ServiceAccount]:
        return self._obj

    @staticmethod
    def from_params(
        params: ServiceAccountAttributes,
    ) -> Optional["ServiceAccountEvent"]:
        try:
            obj = ServiceAccount.readNamespacedServiceAccount(
                name=params.name, namespace=params.namespace
            ).obj
        except Exception:
            logging.error(f"Could not load ServiceAccount {params}", exc_info=True)
            return None
        return ServiceAccountEvent(obj=obj, named_sinks=params.named_sinks)


@dataclass
class ServiceAccountChangeEvent(ServiceAccountEvent, KubernetesAnyChangeEvent):
    obj: Optional[
        Union[v1ServiceAccount, v2beta1ServiceAccount, v2beta2ServiceAccount]
    ] = None
    old_obj: Optional[
        Union[v1ServiceAccount, v2beta1ServiceAccount, v2beta2ServiceAccount]
    ] = None

    def get_serviceaccount(
        self,
    ) -> Optional[
        Union[v1ServiceAccount, v2beta1ServiceAccount, v2beta2ServiceAccount]
    ]:
        return self.obj


KIND_TO_EVENT_CLASS = {
    "Pod": PodChangeEvent,
    "ReplicaSet": ReplicaSetChangeEvent,
    "DaemonSet": DaemonSetChangeEvent,
    "Deployment": DeploymentChangeEvent,
    "StatefulSet": StatefulSetChangeEvent,
    "Service": ServiceChangeEvent,
    "Event": EventChangeEvent,
    "HorizontalPodAutoscaler": HorizontalPodAutoscalerChangeEvent,
    "Node": NodeChangeEvent,
    "ClusterRole": ClusterRoleChangeEvent,
    "ClusterRoleBinding": ClusterRoleBindingChangeEvent,
    "Job": JobChangeEvent,
    "Namespace": NamespaceChangeEvent,
    "ServiceAccount": ServiceAccountChangeEvent,
}
