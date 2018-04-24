########################################################################################
# This file is part of exhale.  Copyright (c) 2017-2018, Stephen McDowell.             #
# Full BSD 3-Clause license available here:                                            #
#                                                                                      #
#                https://github.com/svenevs/exhale/blob/master/LICENSE                 #
########################################################################################

"""
Tests on the ``c_maths`` project.
"""

import os

from testing.base import ExhaleTestCase
from testing.decorators import confoverrides, no_run


class CMathsTests(ExhaleTestCase):
    """
    Primary test class for project ``c_maths``.
    """

    test_project = 'c_maths'
    """
    Index into ``testing/projects``.

    See also: :data:`testing.base.ExhaleTestCase.test_project`.
    """

    def test_app(self):
        """Simply checks :func:`testing.base.ExhaleTestCase.checkRequiredConfigs`."""
        self.checkRequiredConfigs()

    @confoverrides(exhale_args={"containmentFolder": "./alt_api"})
    def test_alt_out(self):
        """
        Test ``"./alt_api"`` rather than default ``"./api"`` as ``"containmentFolder"``.
        """
        self.checkRequiredConfigs()


@no_run
class CMathsTestsNoRun(ExhaleTestCase):
    """
    Secondary test case for project ``c_maths``.

    A :func:`testing.decorators.no_run` decorated test class.
    """

    test_project = 'c_maths'
    """
    Index into ``testing/projects``.

    See also: :data:`testing.base.ExhaleTestCase.test_project`.
    """

    def test_classwide_no_run(self):
        """
        Verify that the default ``"./api"`` folder is indeed **not** generated.
        """
        exhale_args = self.app.config.exhale_args
        containmentFolder = exhale_args['containmentFolder']

        self.assertEqual(containmentFolder, './api')

        # check that nothing has been generated
        api_dir = self.getAbsAgainstSrcdir("containmentFolder")
        self.assertFalse(os.path.exists(api_dir))