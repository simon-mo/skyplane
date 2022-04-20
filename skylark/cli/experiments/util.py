from pathlib import Path

from skylark import skylark_root
from skylark.replicate.solver import ThroughputSolver

import typer


def util_grid_throughput(
    src: str,
    dest: str,
    src_tier: str = "PREMIUM",
    dest_tier: str = "PREMIUM",
    throughput_grid: Path = typer.Option(skylark_root / "profiles" / "throughput.csv", help="Throughput grid file"),
):
    solver = ThroughputSolver(throughput_grid)
    print(solver.get_path_throughput(src, dest, src_tier, dest_tier) / 2**30)


def util_grid_cost(
    src: str,
    dest: str,
    src_tier: str = "PREMIUM",
    dest_tier: str = "PREMIUM",
    throughput_grid: Path = typer.Option(skylark_root / "profiles" / "throughput.csv", help="Throughput grid file"),
):
    solver = ThroughputSolver(throughput_grid)
    print(solver.get_path_cost(src, dest, src_tier, dest_tier))


def get_max_throughput(region_tag: str):
    provider = region_tag.split(":")[0]
    if provider == "aws":
        print(5)
    elif provider == "gcp":
        print(7)
    elif provider == "azure":
        print(16)
    else:
        raise typer.Exit(f"Unknown provider: {provider}")