-- DragonValeHack's All-in-One Lua script for GameGuardian
-- Organized single script with menu for: Item Hack, Resource Hack, Multi-Resource Hack

-- Safety/version gate (optional minimal build only)
gg.require(nil, 0)

-- ------------------------------
-- Data mappings
-- ------------------------------
local ITEM_MAPPING = {
  ["Galaxy Flag"] = 2191473,
  ["Famed Flat Rock"] = 1500,
}

local RESOURCE_MAPPING = {
  ["DragonCash"] = 0,
  ["EXP"] = 2,
  ["Food"] = 4,
  ["Gems"] = 6,
  ["Event Currency"] = 10,
  ["Wishes"] = 12,
  ["Eternal essence"] = 16,
  ["Abundant essence"] = 18,
  ["Vital essence"] = 20,
  ["Ethereum"] = 22,
}

-- ------------------------------
-- Helpers
-- ------------------------------
-- Do NOT override user-selected ranges. Capture current mask to restore after fallbacks.
local INITIAL_RANGES = gg.getRanges()

local function select_item()
  local items = {"Galaxy Flag", "Famed Flat Rock"}
  local idx = gg.choice(items, 1, "Select item")
  if idx == nil then return nil end
  local name = items[idx]
  return {name=name, value=ITEM_MAPPING[name]}
end

local function select_single_resource()
  local keys = {
    "DragonCash","EXP","Food","Gems","Event Currency","Wishes",
    "Eternal essence","Abundant essence","Vital essence","Ethereum"
  }
  local idx = gg.choice(keys, 1, "Select resource")
  if idx == nil then return nil end
  local name = keys[idx]
  return {name=name, skips=RESOURCE_MAPPING[name]}
end

local function select_multi_resources()
  local keys = {
    "DragonCash","EXP","Food","Gems","Event Currency","Wishes",
    "Eternal essence","Abundant essence","Vital essence","Ethereum"
  }
  local sel = gg.multiChoice(keys, {}, "Select resources (multi)")
  if sel == nil then return nil end
  local selected = {}
  for i=1,#keys do
    if sel[i] then selected[#selected+1] = keys[i] end
  end
  table.sort(selected, function(a,b) return RESOURCE_MAPPING[a] < RESOURCE_MAPPING[b] end)
  return selected
end

local function prompt_amount_and_mode(resourceName)
  -- Amount prompt first
  local ret = gg.prompt({"Amount for " .. resourceName}, {[1]=100000}, {[1]="number"})
  if ret == nil then return nil end
  local amt = tonumber(ret[1]) or 0
  if amt <= 0 then gg.alert("Amount must be positive") return nil end
  -- Dropdown for mode selection
  local choice = gg.choice({"Add", "Remove"}, 1, "Select mode")
  if choice == nil then return nil end
  local add = (choice == 1)
  return {amount=amt, add=add}
end

local function prompt_amounts_for_selected(selected)
  local prompts, defaults, types = {}, {}, {}
  for i=1,#selected do
    prompts[i] = "Amount for " .. selected[i]
    defaults[i] = 100000
    types[i] = "number"
  end
  local ret = gg.prompt(prompts, defaults, types)
  if ret == nil then return nil end
  local amounts = {}
  for i=1,#selected do
    local v = tonumber(ret[i]) or 0
    if v > 0 then amounts[selected[i]] = v end
  end
  -- Dropdown for mode selection
  local choice = gg.choice({"Add", "Remove"}, 1, "Select mode")
  if choice == nil then return nil end
  local add = (choice == 1)
  return {amounts=amounts, add=add}
end

local function mode_label(add)
  return add and "Add" or "Remove"
end

local function search_item_qword(val)
  local masks = {
    INITIAL_RANGES, gg.REGION_OTHER
  }

  local function reads_as_target(addr, target)
    local dv = gg.getValues({{address=addr, flags=gg.TYPE_DWORD}})
    if dv and dv[1] and tonumber(dv[1].value) == target then return true end
    local qv = gg.getValues({{address=addr, flags=gg.TYPE_QWORD}})
    if qv and qv[1] and tonumber(qv[1].value) == target then return true end
    return false
  end

  local function filter_by_id(results, target)
    if type(results) ~= "table" or #results == 0 then return nil end
    local filtered = {}
    for i=1,#results do
      if reads_as_target(results[i].address, target) then
        filtered[#filtered+1] = results[i]
      end
    end
    if #filtered > 0 then return filtered end
    return nil
  end

  -- Prefer QWORD in current ranges first (matching Python UI flow), then encrypted, then broaden.
  for _,enc in ipairs({false, true}) do
    gg.clearResults()
    gg.setRanges(INITIAL_RANGES)
    gg.searchNumber(val, gg.TYPE_QWORD, enc, gg.SIGN_EQUAL, 0, -1)
    local count = gg.getResultsCount()
    if count > 0 then
      local res = gg.getResults(count)
      local verified = filter_by_id(res, val)
      if verified then gg.setRanges(INITIAL_RANGES); return verified end
    end
  end

  -- Fallback: broaden masks with QWORD, then try DWORD.
  for i=1,#masks do
    for _,enc in ipairs({false, true}) do
      gg.clearResults()
      gg.setRanges(masks[i])
      gg.searchNumber(val, gg.TYPE_QWORD, enc, gg.SIGN_EQUAL, 0, -1)
      local count = gg.getResultsCount()
      if count > 0 then
        local res = gg.getResults(count)
        local verified = filter_by_id(res, val)
        if verified then gg.setRanges(INITIAL_RANGES); return verified end
      end
    end
  end

  for i=1,#masks do
    for _,enc in ipairs({false, true}) do
      gg.clearResults()
      gg.setRanges(masks[i])
      gg.searchNumber(val, gg.TYPE_DWORD, enc, gg.SIGN_EQUAL, 0, -1)
      local count = gg.getResultsCount()
      if count > 0 then
        local res = gg.getResults(count)
        local verified = filter_by_id(res, val)
        if verified then gg.setRanges(INITIAL_RANGES); return verified end
      end
    end
  end

  -- Restore ranges before giving up.
  gg.setRanges(INITIAL_RANGES)
  return nil
end

local function set_all_zero(results)
  if type(results) ~= "table" or #results == 0 then return end
  local to_set = {}
  for i=1,#results do
    local base = results[i].address
    local addr = base + (0 * 4)
    to_set[#to_set+1] = {address=addr, flags=gg.TYPE_QWORD, value=0}
  end
  gg.setValues(to_set)
end

-- ------------------------------
-- Hack implementations
-- ------------------------------
local function run_item_hack()
  local item = select_item()
  if not item then return end
  local results = search_item_qword(item.value)
  if not results then
    local alt = gg.prompt({"No entries found. Enter item value manually (QWORD)"}, {[1]=ITEM_MAPPING[item.name]}, {[1]="number"})
    if alt ~= nil then
      results = search_item_qword(tonumber(alt[1]) or item.value)
    end
  end
  if not results then gg.alert("No entries found for " .. item.name) return end
  set_all_zero(results)
  gg.alert(string.format("Hacked %d entries for %s.\nNow purchase the item from the store.", #results, item.name), "OK")
end

local function set_direct_cash(results, amount, add)
  local v = add and -amount or amount
  local to_set = {}
  for i=1,#results do
    local base = results[i].address
    local addr = base + (0 * 4)
    to_set[#to_set+1] = {address=addr, flags=gg.TYPE_QWORD, value=v}
  end
  gg.setValues(to_set)
end

local function adjust_single_resource(results, skips, amount, add)
  local delta = add and -amount or amount
  local to_set = {}
  for i=1,#results do
    local base = results[i].address
    local stride = 4
    -- Mapping equals number of lines to skip in Goto; each line is 4 bytes
    local addr = base + (skips * stride)
    to_set[#to_set+1] = {address=addr, flags=gg.TYPE_QWORD, value=delta}
  end
  gg.setValues(to_set)
  return #to_set
end

local function adjust_multiple_resources(results, amounts, add)
  local totalChanged = 0
  for i=1,#results do
    local base = results[i].address
    local batch = {}
    for name, val in pairs(amounts) do
      local skips = RESOURCE_MAPPING[name]
      local stride = 4
      local addr = base + (skips * stride)
      local delta = add and -val or val
      batch[#batch+1] = {address=addr, flags=gg.TYPE_QWORD, value=delta}
    end
    gg.setValues(batch)
    totalChanged = totalChanged + #batch
  end
  return totalChanged
end

local function run_resource_hack()
  local res = select_single_resource(); if not res then return end
  local amt = prompt_amount_and_mode(res.name); if not amt then return end
  local item = select_item(); if not item then return end
  local results = search_item_qword(item.value)
  if not results then
    local alt = gg.prompt({"No entries found. Enter item value manually (QWORD)"}, {[1]=ITEM_MAPPING[item.name]}, {[1]="number"})
    if alt ~= nil then
      results = search_item_qword(tonumber(alt[1]) or item.value)
    end
  end
  if not results then gg.alert("No entries found for " .. item.name) return end
  if #results > 8 then
    gg.alert(string.format("Invalid number of entries found (%d). Please refine search and try again.", #results), "OK")
    return
  end
  if res.name == "DragonCash" then
    set_direct_cash(results, amt.amount, amt.add)
    gg.alert(string.format("Hacked %d entries (%s %s DragonCash).\nNow purchase the item in-game.", #results, mode_label(amt.add), tostring(amt.amount)), "OK")
    return
  end
  -- For non-DragonCash: zero initial records to make item free to purchase
  set_all_zero(results)
  -- Then adjust the resource offsets for all results
  local changed = adjust_single_resource(results, res.skips, amt.amount, amt.add)
  gg.alert(string.format("Hacked %d entries (%s %s %s).\nNow purchase the item in-game.", changed, mode_label(amt.add), tostring(amt.amount), res.name), "OK")
end

local function run_multi_resource_hack()
  local selected = select_multi_resources(); if not selected or #selected == 0 then return end
  local cfg = prompt_amounts_for_selected(selected); if not cfg then return end
  local item = select_item(); if not item then return end
  local results = search_item_qword(item.value)
  if not results then
    local alt = gg.prompt({"No entries found. Enter item value manually (QWORD)"}, {[1]=ITEM_MAPPING[item.name]}, {[1]="number"})
    if alt ~= nil then
      results = search_item_qword(tonumber(alt[1]) or item.value)
    end
  end
  if not results then gg.alert("No entries found for " .. item.name) return end
  if #results > 8 then
    gg.alert(string.format("Invalid number of entries found (%d). Please refine search and try again.", #results), "OK")
    return
  end
  if #selected == 1 and selected[1] == "DragonCash" then
    local cash = cfg.amounts["DragonCash"] or 0
    set_direct_cash(results, cash, cfg.add)
    gg.alert(string.format("Hacked %d entries (%s DragonCash=%s).\nNow purchase the item in-game.", #results, mode_label(cfg.add), tostring(cash)), "OK")
    return
  end
  -- Zero initial records to make item free to purchase
  set_all_zero(results)
  -- Then adjust resource offsets for all selected resources
  local changed = adjust_multiple_resources(results, cfg.amounts, cfg.add)
  -- Build summary list of hacked resources and values in selected order
  local parts = {}
  for i=1,#selected do
    local name = selected[i]
    local val = cfg.amounts[name]
    if val and val > 0 then parts[#parts+1] = name .. "=" .. tostring(val) end
  end
  local summary = table.concat(parts, ", ")
  gg.alert(string.format("Hacked %d entries (%s: %s).\nNow purchase the item in-game.", #results, mode_label(cfg.add), summary), "OK")
end

-- ------------------------------
-- Main menu
-- ------------------------------
local function main_menu()
  local choice = gg.choice({"Item Hack", "Resource Hack", "Multi-Resource Hack", "Exit"}, 1, "DragonVale Hacks")
  if choice == nil or choice == 4 then
    gg.toast("Exiting")
    return
  elseif choice == 1 then
    run_item_hack()
  elseif choice == 2 then
    run_resource_hack()
  elseif choice == 3 then
    run_multi_resource_hack()
  end
end

-- Entry point
main_menu()
