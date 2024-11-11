#pragma once

#include "../base.h"
#ifndef Q_MOC_RUN
#  include <filesystem>
#endif

#ifndef ROLLY_OS_WINDOWS

namespace rolly::oslayer::linux {
  [[nodiscard]] fs::path home_dir();
  [[nodiscard]] fs::path xdg_runtime_dir();
}  // namespace rolly::oslayer::linux

#endif
