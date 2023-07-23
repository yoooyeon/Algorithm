import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> table = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            table.put(players[i], i);
        }
        // System.out.println(table);
        
        for (String calling : callings) {
            Integer post_idx = table.get(calling);
            Integer pre_idx = post_idx - 1;
            for (String key : table.keySet()) {
                if (table.get(key).equals(pre_idx)) {
                    table.put(key, post_idx);
                    break;
                }
            }
            table.put(calling, pre_idx);
        }

        List<Map.Entry<String, Integer>> entryList = new ArrayList<>(table.entrySet());
        Collections.sort(entryList, new Comparator<Map.Entry<String, Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                return o1.getValue().compareTo(o2.getValue());
            }
        });

        String[] result = new String[players.length];
        for (int i = 0; i < entryList.size(); i++) {
            result[i] = entryList.get(i).getKey();
        }

        return result;
    }
}
