import pdb

from urdf_parser_py.sdf import SDF

sdf_tests = ['', 'collision_', 'geometry_', 'joint_', 'link_', 'visual_', 'm0m_0_']
sdf_results = []
for test_name in sdf_tests:
    sdf_path = f"sdf_examples/{test_name}test.sdf"
    print('Testing', sdf_path)
    with open(sdf_path) as f:
        sdf = SDF.from_xml_string(f.read())
    sdf_results.append(sdf)

