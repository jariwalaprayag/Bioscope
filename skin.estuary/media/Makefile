TARGET=Textures.xbt
TARGET_CURIAL=curial.xbt
TARGET_FLAT=flat.xbt

all: $(TARGET) $(TARGET_CURIAL) $(TARGET_FLAT)

.PHONY: force

$(TARGET):
	/build/kodi-jaUjUZ/kodi-17.6+dfsg1/tools/depends/native/TexturePacker/bin/TexturePacker -dupecheck -input . -output $(TARGET)

$(TARGET_CURIAL):
	/build/kodi-jaUjUZ/kodi-17.6+dfsg1/tools/depends/native/TexturePacker/bin/TexturePacker -dupecheck -input ../themes/curial -output $(TARGET_CURIAL)

$(TARGET_FLAT):
	/build/kodi-jaUjUZ/kodi-17.6+dfsg1/tools/depends/native/TexturePacker/bin/TexturePacker -dupecheck -input ../themes/flat -output $(TARGET_FLAT)

clean:
	rm -f $(TARGET)
	rm -f $(TARGET_CURIAL)
	rm -f $(TARGET_FLAT)

distclean: clean
