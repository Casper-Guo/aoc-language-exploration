#include "utils.h"

std::vector<std::string> split(std::string s, char delimiter) {
  std::vector<std::string> splits;
  std::stringstream ss(s);
  std::string word;

  while (!ss.eof()) {
    std::getline(ss, word, delimiter);
    splits.push_back(word);
  }

  return splits;
}

std::string join(std::vector<std::string> v, std::string joiner) {
  std::string s;

  for (size_t i = 0; i < v.size() - 1; i++) {
    s += (v[i] + joiner);
  }
  s += v[v.size() - 1];
  return s;
}

std::vector<std::string> split_csv(std::string s) {
  // assuming the following format
  // <item1>, <item2>, <item3>...
  std::vector<std::string> splits = split(s);
  for (size_t i = 0; i < splits.size(); ++i) {
    if (splits[i].find(',') != std::string::npos) {
      splits[i] = splits[i].substr(0, splits[i].length() - 1);
    }
  }

  return splits;
}

std::map<char, int> char_freq(std::string s) {
  std::map<char, int> freq_count;
  for (char i : s) {
    if (freq_count.find(i) != freq_count.end()) {
      freq_count[i] += 1;
    } else {
      freq_count[i] = 1;
    }
  }

  return freq_count;
}

std::vector<std::string> readlines(std::ifstream& f) {
  std::vector<std::string> lines;
  std::string line;

  while (std::getline(f, line)) {
    lines.push_back(line);
  }

  return lines;
}

bool is_int(const char& c) { return std::isdigit(c); }

bool is_int(const std::string& s) {
  std::string::const_iterator it;
  if (s[0] == '+' || s[0] == '-') {
    it = s.begin() + 1;
  } else {
    it = s.begin();
  }
  while (it != s.end() && std::isdigit(*it)) ++it;
  return !s.empty() && it == s.end();
}

std::string md5(const std::string& str) {
  unsigned char hash[MD5_DIGEST_LENGTH];

  MD5_CTX md5;
  MD5_Init(&md5);
  MD5_Update(&md5, str.c_str(), str.size());
  MD5_Final(hash, &md5);

  std::stringstream ss;

  for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
    ss << std::hex << std::setw(2) << std::setfill('0')
       << static_cast<int>(hash[i]);
  }
  return ss.str();
}