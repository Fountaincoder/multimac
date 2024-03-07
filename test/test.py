# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


# DMADD madd(
        # .clk    (clk),
        # .run    (uio_in[3]),
        # .load   (uio_in[2]),
        # .insn   (uio_in[1:0]),
        # .index  (ui_in[7:4]),
        # .data   (ui_in[3:0]),
        # .out    ({uio_out[7:4],uo_out}),
        # .rst_n  (rst_n)
# );
# 

@cocotb.test()
async def test_15(dut):
    dut._log.info("Start 15")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())
    # Reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk,100)
    dut.ena.value = 1
    dut.rst_n.value = 1
    dut.uio_in.value = 0b0000_0_1_00
    dut.ui_in.value = 0b1111_1111
    await ClockCycles(dut.clk,100 )
    dut.uio_in.value = 0b0000_1_0_00
    await ClockCycles(dut.clk,100 )
    dut._log.info(dut.uo_out.value)
    assert(dut.uo_out.value==0b1111)

# @cocotb.test()
# async def test_1(dut):
    # dut._log.info("Start 1")
  # 
    # # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    # clock = Clock(dut.clk, 10, units="us")
    # cocotb.start_soon(clock.start())
    # dut.rst_n.value = 0
    # await ClockCycles(dut.clk,100)
    # dut.ena.value = 1
    # dut.rst_n.value = 1
    # dut.uio_in.value = 0b0000_0_1_00
    # dut.ui_in.value = 0b0001_0000
    # await ClockCycles(dut.clk,100 )
    # dut.uio_in.value = 0b0000_1_0_00
    # await ClockCycles(dut.clk,100 )
    # dut._log.info(dut.uo_out.value)
    # assert(dut.uo_out.value==0b0001)
# 
# @cocotb.test()
# async def test_78(dut):
    # dut._log.info("Start 78")
  # 
    # # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    # 
    # clock = Clock(dut.clk, 10, units="us")
    # cocotb.start_soon(clock.start())
    # dut.rst_n.value = 0
    # await ClockCycles(dut.clk,100)
    # # Reset
    # dut.ena.value = 1
    # dut.rst_n.value = 1
    # dut.uio_in.value = 0b0000_0_1_00
    # dut.ui_in.value = 0b0111_0000
    # await ClockCycles(dut.clk,100 )
    # dut.ui_in.value = 0b1000_0000
    # await ClockCycles(dut.clk,100 )
    # dut.uio_in.value = 0b0000_1_0_00
    # await ClockCycles(dut.clk,100 )
    # dut._log.info(dut.uo_out.value)
    # assert(dut.uo_out.value==0b0111)
# 
# @cocotb.test()
# async def test_8(dut):
    # dut._log.info("Start 78")
  # 
    # # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    # 
    # clock = Clock(dut.clk, 10, units="us")
    # cocotb.start_soon(clock.start())
    # dut.rst_n.value = 0
    # await ClockCycles(dut.clk,100)
    # # Reset
    # dut.ena.value = 1
    # dut.rst_n.value = 1
    # dut.uio_in.value = 0b0000_0_1_00
    # dut.ui_in.value = 0b1000_0000
    # await ClockCycles(dut.clk,100 )
    # dut.uio_in.value = 0b0000_1_0_00
    # await ClockCycles(dut.clk,100 )
    # dut._log.info(dut.uo_out.value)
    # assert(dut.uo_out.value==0b1000)
