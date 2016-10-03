#!/usr/bin/python

import Foundation
import objc
import AppKit
import sys

sys.dont_write_bytecode =  True

NSUserNotification = objc.lookUpClass('NSUserNotification')
NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

def notify(title, subtitle, info_text, delay=0, sound=False, userInfo={}):
	notification = NSUserNotification.alloc().init()
	notification.setTitle_(title)
	notification.setSubtitle_(subtitle)
	notification.setInformativeText_(info_text)
	notification.setUserInfo_(userInfo)

	if sound:
		notification.setSoundName_("NSUserNotificationDefaultSoundName")
	notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
	NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

def clearNotifications():
        """Clear any displayed alerts we have posted. Requires Mavericks."""

        NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
        NSUserNotificationCenter.defaultUserNotificationCenter().removeAllDeliveredNotifications()

clearNotifications()
