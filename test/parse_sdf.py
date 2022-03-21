import os
import pdb

from urdf_parser_py.sdf import SDF

sdf_tests = ["", "collision_", "geometry_", "joint_", "link_", "visual_", "m0m_0_"]
sdf_results = []


def load_sdf_examples():
    sdf_examples_dir = os.path.join(os.path.dirname(__file__), "sdf_examples")

    for test_name in sdf_tests:
        sdf_path = os.path.join(sdf_examples_dir, f"{test_name}test.sdf")
        print("Testing", sdf_path)
        with open(sdf_path) as f:
            sdf = SDF.from_xml_string(f.read())
        sdf_results.append(sdf)


if __name__ == "__main__":
    load_sdf_examples()
