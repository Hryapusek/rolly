#pragma once

#include <leaf/global.h>

namespace leaf::conversion
{
  using std::string;
  using std::string_view;

  template<typename From, typename To>
  [[nodiscard]] auto into(From) -> To { throw std::runtime_error("unimplemented conversion"); }

  template<typename T>
  [[nodiscard]] auto from_str(string_view) -> T { throw std::runtime_error("unimplemented conversion"); }

  template<typename T>
  [[nodiscard]] auto try_from_str(string_view) -> expected<T, string> { throw std::runtime_error("unimplemented conversion"); }

  template<typename T>
  [[nodiscard]] auto as_str(T) -> string { throw std::runtime_error("unimplemented conversion"); }

  template<typename T>
  [[nodiscard]] auto try_as_str(T) -> string { throw std::runtime_error("unimplemented conversion"); }
}

namespace leaf::conversion
{
  template<> [[nodiscard]] auto into(const types::u8 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::i8 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::u16 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::i16 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::u32 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::i32 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::u64 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::i64 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::f32 from) -> std::string { return std::to_string(from); }
  template<> [[nodiscard]] auto into(const types::f64 from) -> std::string { return std::to_string(from); }
}