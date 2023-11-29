# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/oracle/v1/event.proto, cosmos/oracle/v1/genesis.proto, cosmos/oracle/v1/oracle.proto, cosmos/oracle/v1/query.proto, cosmos/oracle/v1/tx.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List, Optional

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class ClaimSrcChain(betterproto.Enum):
    """ClaimSrcChain defines the src chain of a claim"""

    CLAIM_SRC_CHAIN_UNSPECIFIED = 0
    """CLAIM_SRC_CHAIN_UNSPECIFIED"""

    CLAIM_SRC_CHAIN_BSC = 1
    """CLAIM_SRC_CHAIN_BSC defines BSC source chain"""

    CLAIM_SRC_CHAIN_OP_BNB = 2
    """CLAIM_SRC_CHAIN_OP_BNB defines OPBNB source chain"""


@dataclass(eq=False, repr=False)
class EventPackageClaim(betterproto.Message):
    """EventPackageClaim is emitted when a cross chain package is processed"""

    src_chain_id: int = betterproto.uint32_field(1)
    """Source chain id of the package"""

    dest_chain_id: int = betterproto.uint32_field(2)
    """Destination chain id of the package"""

    channel_id: int = betterproto.uint32_field(3)
    """Channel id of the package"""

    package_type: int = betterproto.uint32_field(4)
    """Package type of the package, like SYN, ACK and FAIL_ACK"""

    receive_sequence: int = betterproto.uint64_field(5)
    """Receive sequence of the package"""

    send_sequence: int = betterproto.int64_field(6)
    """Send sequence of the corresponding ACK package or FAIL_ACK package"""

    crash: bool = betterproto.bool_field(7)
    """Crash status for the handle of this package"""

    error_msg: str = betterproto.string_field(8)
    """Error message for the handle of this package"""

    relayer_fee: str = betterproto.string_field(9)
    """Relayer fee paid for this package"""

    ack_relayer_fee: str = betterproto.string_field(10)
    """Relayer fee paid for the ACK or FAIL_ACK package"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the oracle module."""

    relayer_timeout: int = betterproto.uint64_field(1)
    """Timeout for the in turn relayer in seconds"""

    relayer_interval: int = betterproto.uint64_field(2)
    """RelayInterval is for in-turn relayer in seconds"""

    relayer_reward_share: int = betterproto.uint32_field(3)
    """
    Reward share for the relayer sends the claim message,
    the other relayers signed the bls message will share the reward evenly.
    """


@dataclass(eq=False, repr=False)
class RelayInterval(betterproto.Message):
    """
    RelayInterval holds start and end(exclusive) time of in-turn relayer, [start, end)
    """

    start: int = betterproto.uint64_field(1)
    end: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the oracle module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the parameters of related to oracle module."""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    params: "Params" = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class QueryInturnRelayerRequest(betterproto.Message):
    """
    QueryInturnRelayerRequest is the request type for the Query In-turn relayer RPC
    method.
    """

    claim_src_chain: "ClaimSrcChain" = betterproto.enum_field(1)
    """ClaimSrcChain defines the src chain of a claim"""


@dataclass(eq=False, repr=False)
class QueryInturnRelayerResponse(betterproto.Message):
    """
    QueryInturnRelayerResponse is the response type for the Query In-turn relayer RPC
    method.
    """

    bls_pub_key: str = betterproto.string_field(1)
    relay_interval: "RelayInterval" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgClaim(betterproto.Message):
    """MsgClaim defines the Msg/Claim request type"""

    from_address: str = betterproto.string_field(1)
    """sender address of the msg"""

    src_chain_id: int = betterproto.uint32_field(2)
    """source chain id"""

    dest_chain_id: int = betterproto.uint32_field(3)
    """destination chain id"""

    sequence: int = betterproto.uint64_field(4)
    """sequence of the oracle channel"""

    timestamp: int = betterproto.uint64_field(5)
    """timestamp of the claim"""

    payload: bytes = betterproto.bytes_field(6)
    """payload of the claim"""

    vote_address_set: List[int] = betterproto.fixed64_field(7)
    """bit map of the voted validators"""

    agg_signature: bytes = betterproto.bytes_field(8)
    """bls signature of the claim"""


@dataclass(eq=False, repr=False)
class MsgClaimResponse(betterproto.Message):
    """MsgClaimResponse defines the Msg/Claim response type"""

    pass


@dataclass(eq=False, repr=False)
class MsgUpdateParams(betterproto.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless
    overwritten).
    """

    params: "Params" = betterproto.message_field(2)
    """
    params defines the x/crosschain parameters to update.
    NOTE: All parameters must be supplied.
    """


@dataclass(eq=False, repr=False)
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.oracle.v1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def inturn_relayer(
        self,
        query_inturn_relayer_request: "QueryInturnRelayerRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryInturnRelayerResponse":
        return await self._unary_unary(
            "/cosmos.oracle.v1.Query/InturnRelayer",
            query_inturn_relayer_request,
            QueryInturnRelayerResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def claim(
        self,
        msg_claim: "MsgClaim",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgClaimResponse":
        return await self._unary_unary(
            "/cosmos.oracle.v1.Msg/Claim",
            msg_claim,
            MsgClaimResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_params(
        self,
        msg_update_params: "MsgUpdateParams",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgUpdateParamsResponse":
        return await self._unary_unary(
            "/cosmos.oracle.v1.Msg/UpdateParams",
            msg_update_params,
            MsgUpdateParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def params(self, query_params_request: "QueryParamsRequest") -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def inturn_relayer(
        self, query_inturn_relayer_request: "QueryInturnRelayerRequest"
    ) -> "QueryInturnRelayerResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]") -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_inturn_relayer(
        self,
        stream: "grpclib.server.Stream[QueryInturnRelayerRequest, QueryInturnRelayerResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.inturn_relayer(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.oracle.v1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.oracle.v1.Query/InturnRelayer": grpclib.const.Handler(
                self.__rpc_inturn_relayer,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryInturnRelayerRequest,
                QueryInturnRelayerResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def claim(self, msg_claim: "MsgClaim") -> "MsgClaimResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_params(self, msg_update_params: "MsgUpdateParams") -> "MsgUpdateParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_claim(self, stream: "grpclib.server.Stream[MsgClaim, MsgClaimResponse]") -> None:
        request = await stream.recv_message()
        response = await self.claim(request)
        await stream.send_message(response)

    async def __rpc_update_params(
        self, stream: "grpclib.server.Stream[MsgUpdateParams, MsgUpdateParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.oracle.v1.Msg/Claim": grpclib.const.Handler(
                self.__rpc_claim,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgClaim,
                MsgClaimResponse,
            ),
            "/cosmos.oracle.v1.Msg/UpdateParams": grpclib.const.Handler(
                self.__rpc_update_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateParams,
                MsgUpdateParamsResponse,
            ),
        }
